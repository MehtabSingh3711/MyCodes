class TextEditor:
    def __init__(self):
        self.content = ""
        self.undo_stack = []
        self.redo_stack = []

    def add_text(self, text):
        # Action: Add text
        self.content += text
        self.undo_stack.append(("ADD", text))
        self.redo_stack.clear()  # Clear redo history after a new action
        print(f"Added text: '{text}'\nCurrent content: '{self.content}'")

    def delete_text(self, length):
        # Action: Delete last `length` characters
        deleted_text = self.content[-length:]
        self.content = self.content[:-length]
        self.undo_stack.append(("DELETE", deleted_text))
        self.redo_stack.clear()
        print(f"Deleted text: '{deleted_text}'\nCurrent content: '{self.content}'")

    def undo(self):
        if self.undo_stack:
            action, value = self.undo_stack.pop()
            if action == "ADD":
                # Undo adding text: Remove the added text
                self.content = self.content[:-len(value)]
                self.redo_stack.append(("ADD", value))
            elif action == "DELETE":
                # Undo deleting text: Add the deleted text back
                self.content += value
                self.redo_stack.append(("DELETE", value))
            print(f"Undo '{action}': {value}\nCurrent content: '{self.content}'")
        else:
            print("No actions to undo.")

    def redo(self):
        if self.redo_stack:
            action, value = self.redo_stack.pop()
            if action == "ADD":
                # Redo adding text
                self.content += value
                self.undo_stack.append(("ADD", value))
            elif action == "DELETE":
                # Redo deleting text
                self.content = self.content[:-len(value)]
                self.undo_stack.append(("DELETE", value))
            print(f"Redo '{action}': {value}\nCurrent content: '{self.content}'")
        else:
            print("No actions to redo.")

# Testing the TextEditor class with complex Undo-Redo

editor = TextEditor()

# Performing actions
editor.add_text("Hello ")
editor.add_text("World!")
editor.delete_text(6)  # Deletes "World!"
editor.undo()  # Undo delete "World!"
editor.undo()  # Undo adding "World!"
editor.redo()  # Redo adding "World!"
editor.add_text("Python")
editor.undo()  # Undo adding "Python"
editor.redo()  # Redo adding "Python"
