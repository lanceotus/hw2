import ast
import os
import collections

from words_count import service_funcs


class WordsCount:
    def __init__(self, pos, name_type, language):
        self.pos = pos
        self.name_type = name_type
        self.language = language

    def get_filenames(self, dirpath):
        filenames = []
        for dirname, dirs, files in os.walk(dirpath, topdown=True):
            for file in files:
                if len(filenames) == 100:
                    return filenames
                if service_funcs.is_this_language(file, self.language):
                    filenames.append(os.path.join(dirname, file))
        return filenames

    def _get_words_parsing_trees(self, dirpath, with_filenames=False, with_file_content=False):
        trees = []
        filenames = self.get_filenames(dirpath)
        print('total %s files' % len(filenames))
        for filename in filenames:
            with open(filename, 'r', encoding='utf-8') as attempt_handler:
                main_file_content = attempt_handler.read()
            try:
                tree = ast.parse(main_file_content)
            except SyntaxError as e:
                print(e)
                tree = None
            if with_filenames:
                if with_file_content:
                    trees.append((filename, main_file_content, tree))
                else:
                    trees.append((filename, tree))
            else:
                trees.append(tree)
        print('trees generated')
        return trees

    def _get_names(self, tree):
        if self.name_type == "functions":
            return self._get_function_names(tree)
        elif self.name_type == "variables":
            return self._get_variable_names(tree)

    @staticmethod
    def _get_function_names(tree):
        return [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

    @staticmethod
    def _get_variable_names(tree):
        functions_bodies = [node.body for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        varnames = []
        for fb in functions_bodies:
            for a in fb:
                if isinstance(a, ast.Assign) and isinstance(a.targets[0], ast.Name):
                    varnames.append(a.targets[0].id)
        return varnames

    def is_proper_pos(self, word):
        if self.pos == "verb":
            return service_funcs.is_verb(word)
        elif self.pos == "noun":
            return service_funcs.is_noun(word)
        else:
            return False

    def get_pos_from_name(self, name):
        return [word for word in name.split('_') if self.is_proper_pos(word)]

    def get_stats(self, dirpath):
        trees = self._get_words_parsing_trees(dirpath)
        names = []
        for tr in trees:
            names += self._get_names(tr)
        poslist = service_funcs.flat([self.get_pos_from_name(name) for name in names
                                     if not service_funcs.is_reserved_name(name)])
        raw_res = collections.Counter(poslist).most_common()
        res = {"headers":[self.pos, "count"], "body":{}}
        for word, occurence in raw_res:
            res["body"][word] = occurence
        return res
