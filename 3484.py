class Spreadsheet:

    def __init__(self, rows: int):
        self._sheet = [[0] * 26 for _ in range(rows)]

    def _getCell(self, cell: str) -> tuple[int, int, int]:
        row, col = int(cell[1:]) - 1, ord(cell[0]) - 65
        return int(self._sheet[row][col]), row, col

    def setCell(self, cell: str, value: int) -> None:
        _, row, col = self._getCell(cell)
        self._sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        cells = formula[1:].split('+')
        c0 = int(cells[0]) if cells[0].isdigit() else self._getCell(cells[0])[0]
        c1 = int(cells[1]) if cells[1].isdigit() else self._getCell(cells[1])[0]
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
