from library.DataHandling import excel_handling

def ConstantsVariables():

	excelPath = "../data/test_data.xlsx"
	ChromeKey = excel_handling(2, 2, 'Sheet5', excelPath)  # Row num, Col Num, Sheet Name, Excel File Name
	MozilaKey = excel_handling(3, 2, 'Sheet5', excelPath)  # Row num, Col Num, Sheet Name, Excel File Name
	return MozilaKey