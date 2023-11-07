import string
import xlrd
loa_check_address = ["LOA Summary", "A", 1]
npt_check_address = ["Offer_Information", "B", 11]

class ExcelObject(object):

    def __init__(self, path):
        self.workbook = xlrd.open_workbook(path, 'rb')
        self.sheets = self.workbook.sheet_names()

    def which_row_has(self, text, sheet, column):
        worksheet = self.workbook.sheet_by_name(sheet)
        for row in range(worksheet.nrows):
            if self.get_value(sheet, row, column) == text:
                return row

    def get_value(self, sheet, row, column):
        if self.check_sheet_exist(sheet):
            worksheet = self.workbook.sheet_by_name(sheet)
            value = worksheet.cell(row - 1, column - 1).value
        else:
            value = None
        return value

    def check_sheets_exist(self, names):
        for sheet in names:
            if sheet not in self.sheets:
                return False
        return True

    def check_sheet_exist(self, name):
        if name in self.sheets:
            return True
        return False

    def is_loa(self):
        sheet = self.get_sheet(loa_check_address)
        column = self.get_column(loa_check_address)
        row = self.get_row(loa_check_address)
        loa_op = self.get_value(sheet, row, column)
        return loa_op == 'OP'

    def is_npt(self):
        sheet = self.get_sheet(npt_check_address)
        column = self.get_column(npt_check_address)
        row = self.get_row(npt_check_address)
        npt_oi = self.get_value(sheet, row, column)
        return npt_oi == 'Offer Information'

    @staticmethod
    def column_to_number(column):
        num = 0
        for col in column:
            if col in string.ascii_letters:
                num = num * 26 + (ord(col.upper()) - ord('A')) + 1
        return num

    @staticmethod
    def get_sheet(address_list):
        return address_list[0]

    @staticmethod
    def get_row(address_list):
        return int(address_list[2])

    @staticmethod
    def get_column(address_list):
        if type(address_list) == list:
            column_letter = str(address_list[1])
        else:
            column_letter = str(address_list)
        column = ExcelObject.column_to_number(column_letter)
        return int(column)
