def congratulations(project_manager, tester, *args):
    print('Happy New Year! Take care of yourself and your loved ones! \n For:\n')
    print(project_manager)
    print(tester)
    for n in args:
        print(n)


congratulations('Alice','Mike','Joe','Vic')

#ou plus simplement :
#def congratulations(manager, tester, *developer):
    #print(f"Happy New Year! Take care of yourself and your loved ones!\n For: \n{manager} \n{tester}", *developer, sep="\n")
