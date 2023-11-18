GMAPS_URL ="https://www.google.com/maps/@32.0851663,34.8955189,15z?authuser=0&entry=ttu" 
auto = Automaps(GMAPS_URL)
LIST_NAME = "Bouldering"
'''
#driver = launch_gmaps()
# with open("addresses_wrk_cpy.txt", 'rt') as ADDR_FILE:
notes = open("notes.txt",'rt')
with open("testfile.txt", 'rt') as ADDR_FILE:
    for address in ADDR_FILE:

        note = notes.readline()
        
        auto.enter_address(address)

        # Click "save" button (opens save-dropdown menu) & save to 'bombshelters' list
        time.sleep(1)
        try:
            # adding notes modification:
            # auto.save_to_list(LIST_NAME)
            auto.add_note(note)

        except Exception as e:
            print(e, " coudn't add: " + address)
        time.sleep(1) 
        # Clear searchbox
        auto.clear_searchbar()
'''
auto.enter_address("orlife")
time.sleep(2)
try:
    # auto.save_to_list()
    pass
except Exception as e:
    print(e)
time.sleep(4)
auto.driver.quit()
# notes.close()
