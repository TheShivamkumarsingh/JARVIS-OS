import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}


class SafeMath:

    def evaluate(self, expression: str):

        tree = ast.parse(expression, mode="eval")

        return self._eval(tree.body)

    def _eval(self, node):

        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.BinOp):
            left = self._eval(node.left)
            right = self._eval(node.right)

            return OPERATORS[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp):
            operand = self._eval(node.operand)

            return OPERATORS[type(node.op)](operand)

        raise ValueError("Unsupported expression")