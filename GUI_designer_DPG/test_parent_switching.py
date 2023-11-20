import dearpygui.dearpygui as dpg

# DPG GUI
dpg.create_context()
dpg.create_viewport(title="Test")
dpg.setup_dearpygui()

# Custom Functions
def delete_parent():
    dpg.delete_item(item=parent_tag)

def restore_parent():
    print(dpg.does_item_exist(parent_tag))
    #dpg.add_window(label="Test Parent", tag=parent_tag)

def restore_child():
    print(dpg.does_item_exist(group_tag))
    print(dpg.does_item_exist(child_tag))
    #dpg.add_button(label="Child Button", parent=parent_tag, tag=child_tag, callback=do_something)

def do_something(sender):
    print(sender)
    print("Child!")

# Custom Test
parent_tag = dpg.add_window(label="Test Parent")
group_tag = dpg.add_group(label="Test Group", parent=parent_tag)
child_tag = dpg.add_button(label="Child Button", parent=group_tag, callback=do_something)

control_tag = dpg.add_window(label="Test Control")
dpg.add_button(label="Delete Parent", parent=control_tag, callback=delete_parent)
dpg.add_button(label="Restore Parent", parent=control_tag, callback=restore_parent)
dpg.add_button(label="Restore Child", parent=control_tag, callback=restore_child)


# DPG GUI Start and Cleanup
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()