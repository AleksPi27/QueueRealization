# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Queue import Queue
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    q=Queue()
    print("Top element is", q.top())
    q.push(1)
    print("Top element is", q.top())
    q.push(2)

    q.push(3)
    print("Top element is", q.top())

    for i in range(0,10):
        q.push(i)
        print("Top element is", q.top())
    print("Deleting all elements")
    for i in range(q.size()):
        q.pop()
    print(q.top())
    print(q.isEmpty())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
