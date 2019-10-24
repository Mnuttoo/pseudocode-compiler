class AST(object):
    pass


class Block(AST):
    def __init__(self, statement_list):
        self.block = statement_list


class Statement(AST):
    def __init__(self, statement):
        self.statement = statement


class EmptyLine(AST):
    def __init__(self, token):
        self.token = token


class BinaryOperation(AST):
    def __init__(self, left, operation, right):
        self.left = left
        self.token = self.operation = operation
        self.right = right


class UnaryOperation(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr


class Value(AST):
    def __init__(self, token):
        self.token = token

# START: Variable Declaration


class Declarations(AST):
    def __init__(self, variable_declarations):
        self.declarations = variable_declarations


class VariableDeclaration(AST):
    def __init__(self, variable, data_type):
        self.variable = variable
        self.data_type = data_type


class DataType(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Array(AST):
    def __init__(self, dimensions, data_type):
        self.dimensions = dimensions
        self.data_type = data_type


class Dimensions(AST):
    def __init__(self, dimensions):
        self.dimensions = dimensions


class Dimension(AST):
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound


class Bound(AST):
    def __init__(self, bound):
        self.value = bound


class Index(AST):
    def __init__(self, index):
        self.index = index

# END: Variable Declaration

# START: Variable Assignment


class Assignment(AST):
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression


class VariableValue(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class VariableName(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class ElementName(AST):
    def __init__(self, variable, indexes):
        self.variable = variable
        self.indexes = indexes
        self.value = variable.value


class ElementValue(AST):
    def __init__(self, variable, indexes):
        self.variable = variable
        self.indexes = indexes
        self.value = variable.value


class AssignArray(AST):
    def __init__(self, array):
        self.array = array

# END: Variable Assignment

# START: Input


class AssignInput(AST):
    def __init__(self, input_node):
        self.input_node = input_node


class Input(AST):
    def __init__(self, input_string, variable):
        self.input_string = input_string
        self.variable = variable

# END: Input

# START: Output


class Output(AST):
    def __init__(self, output):
        self.output = output

# END: Output

# START: Logical Operations


class BinaryLogicalOperation(AST):
    def __init__(self, left, logical_operation, right):
        self.left = left
        self.logical_operation = logical_operation
        self.right = right


class UnaryLogicalOperation(AST):
    def __init__(self, logical_operation, condition):
        self.logical_operation = logical_operation
        self.condition = condition


class Condition(AST):
    def __init__(self, left, comparison, right):
        self.left = left
        self.comparison = comparison
        self.right = right

# END: Logical Operations

# START: Selection


class Selection(AST):
    def __init__(self, selection_list):
        self.selection_list = selection_list


class SelectionStatement(AST):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

# END: Selection

# START: Case


class Case(AST):
    def __init__(self, case_list):
        self.case_list = case_list


class CaseStatement(AST):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block


class Options(AST):
    def __init__(self, options):
        self.options = options


class Range(AST):
    def __init__(self, start, end):
        self.start = start
        self.end = end

# END: Case

# START: Iteration


class Iteration(AST):
    def __init__(self, variable, assignment, end, step, block):
        self.variable = variable
        self.assignment = assignment
        self.end = end
        self.step = step
        self.block = block

# END: Iteration

# START: Loop


class Loop(AST):
    def __init__(self, condition, block, loop_while):
        self.condition = condition
        self.block = block
        self.loop_while = loop_while

# END: Loop

# START: Built-in Function


class BuiltInFunction(AST):
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
        self.parsed_parameters = None

# END: Built-in Function


class Parameter(AST):
    def __init__(self, variable, data_type, scope_type):
        self.variable = variable
        self.data_type = data_type
        self.scope_type = scope_type

# START: Procedure/Function


class FunctionCall(AST):
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters


class Function(AST):
    def __init__(self, name, parameters, block, return_type):
        self.name = name
        self.parameters = parameters
        self.block = block
        self.return_type = return_type

# END: Procedure/Function

# START: File


class File(AST):
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode


class FileMode(AST):
    def __init__(self, file_mode):
        self.file_mode = file_mode


class ReadFile(AST):
    def __init__(self, file_name, variable):
        self.file_name = file_name
        self.variable = variable


class WriteFile(AST):
    def __init__(self, file_name, line):
        self.file_name = file_name
        self.line = line


class CloseFile(AST):
    def __init__(self, file_name):
        self.file_name = file_name

# START: Type


class TypeDeclaration(AST):
    def __init__(self, type_name, block):
        self.type_name = type_name
        self.block = block


class TypeName(AST):
    def __init__(self, object_, property_):
        self.object_ = object_
        self.property_ = property_


class TypeValue(AST):
    def __init__(self, object_, property_):
        self.object_ = object_
        self.property_ = property_

 # END: Type
