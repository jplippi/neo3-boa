from typing import List, Optional

from boa3.model.operation.binary.binaryoperation import BinaryOperation
from boa3.model.operation.operator import Operator
from boa3.model.type.type import IType, Type
from boa3.neo.vm.opcode.Opcode import Opcode


class Concat(BinaryOperation):
    """
    A class used to represent a string concatenation operation

    :ivar operator: the operator of the operation. Inherited from :class:`IOperation`
    :ivar left: the left operand type. Inherited from :class:`BinaryOperation`
    :ivar right: the left operand type. Inherited from :class:`BinaryOperation`
    :ivar result: the result type of the operation.  Inherited from :class:`IOperation`
    """
    _valid_types: List[IType] = [Type.str]

    def __init__(self, left: IType = Type.str, right: IType = Type.str):
        self.operator: Operator = Operator.Plus
        super().__init__(left, right)

    def validate_type(self, *types: IType) -> bool:
        if len(types) != self._get_number_of_operands:
            return False
        left: IType = types[0]
        right: IType = types[1]

        return left == right and left in self._valid_types

    def _get_result(self, left: IType, right: IType) -> IType:
        if self.validate_type(left, right):
            return left
        else:
            return Type.none

    @property
    def opcode(self) -> Optional[Opcode]:
        return Opcode.CAT

    @property
    def is_supported(self) -> bool:
        # TODO: change when concat is supported
        return False
