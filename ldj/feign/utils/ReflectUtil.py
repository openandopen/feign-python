#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 15:02

import ast
import inspect

class ReflectUtil:

    @staticmethod
    def get_decorators(cls):
        target = cls
        decorators = {}

        def visit_FunctionDef(node):
            decorators[node.name] = []
            for n in node.decorator_list:
                name = ''
                print(n.func)
                if isinstance(n, ast.Call):
                    name = n.func.attr if isinstance(n.func, ast.Attribute) else n.func.id
                else:
                    name = n.attr if isinstance(n, ast.Attribute) else n.id
                decorators[node.name].append(name)

        node_iter = ast.NodeVisitor()
        node_iter.visit_FunctionDef = visit_FunctionDef
        node_iter.visit(ast.parse(inspect.getsource(target)))
        return decorators
