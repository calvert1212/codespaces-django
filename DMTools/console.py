# The main console for using DMTools
sesh = bool(1);

while(sesh == 1):
    op = input(('Console: Choose an option\n lg for LootGen\nexit to exit\n'))
    def choice(op):
       if op == "lg":
        import DMTools.lootGen as lootGen;
       elif op == "exit":
        sesh = (0)