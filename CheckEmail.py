def check_email(string):
    return " " not in string and "@" in string and string.startswith(".",string.rfind(".")) and string.index("@")+1<string.rfind(".")

#ou en moins simple:
'''def check_email(string):
    if " " not in string:
        test = "OK"
        if "@" in string:
            test = "OK2"
            if string.startswith(".",string.rfind(".")):
                index_dot = string.rfind(".")
                test = "OK3"
                if (string.index("@")+1)<index_dot:
                    test = "OK4"
    else:
        test = "FAIL"
    if test != "OK4":
        return False
    else:
        return True'''

check_email('good.email@example.com')