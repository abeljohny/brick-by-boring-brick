class Spreadsheet:

    def __init__(self, rows: int):
        self._sheet = [[0] * 26 for _ in range(rows)]

    def _getCell(self, cell: str) -> tuple[int, int]:
        return ord(cell[0]) - 65, int(cell[1:]) - 1

    def setCell(self, cell: str, value: int) -> None:
        col, row = self._getCell(cell)
        self._sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        cells = formula[1:].split('+')
        if cells[0].isdigit():
            c0 = int(cells[0])
        else:
            c0_col, c0_row = self._getCell(cells[0])
            c0 = int(self._sheet[c0_row][c0_col])

        if cells[1].isdigit():
            c1 = int(cells[1])
        else:
            c1_col, c1_row = self._getCell(cells[1])
            c1 = int(self._sheet[c1_row][c1_col])

        return c0 + c1


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(3)
# print(obj.getValue('=5+7'))
# obj.setCell('A1',10)
# print(obj.getValue('=A1+6'))
# obj.setCell('B2',15)
# print(obj.getValue('=A1+B2'))
# obj.resetCell('A1')
# print(obj.getValue('=A1+B2'))
