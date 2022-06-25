import configparser
cnfg = configparser.ConfigParser()
cnfg.optionxform = str
cnfg['PATHS'] = {'DIR': r"C:\Users\alanm\OneDrive\Desktop\ADSP_Project\Test_folder\test_files",
        'PM_LOCATE': r"C:\Users\alanm\OneDrive\Desktop\ADSP_Project\Test_folder\pm_file.txt",
        'DM_LOCATE': r"C:\Users\alanm\OneDrive\Desktop\ADSP_Project\Test_folder\dm_file.txt",
        'DMrdfl_LOCATE': r"C:\Users\alanm\OneDrive\Desktop\ADSP_Project\Test_folder\DMrd",
        'MEMfail_LOCATE': r"C:\Users\alanm\OneDrive\Desktop\ADSP_Project\Test_folder\MEMfail"}
cnfg['IDENTIFIER'] = {'idntfr': "_"}
cnfg['AVOID'] = {'pm_file.txt': "",
        'dm_file.txt': ""}
with open('Path.ini', 'w') as pathfl:
    cnfg.write(pathfl)
