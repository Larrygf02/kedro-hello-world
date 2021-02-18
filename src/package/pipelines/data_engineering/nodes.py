from kedro.pipeline import node

# Prepare first node
def return_greeting():
    return 'Hello'

return_greeting_node = node(
    func=return_greeting,
    inputs=None,
    outputs="my_salutation",
    name="return_greeting_node"
)

# Prepare second node
def join_statements(gretting):
    return f"{gretting} Kedro!"

join_statements_node = node(
    func=join_statements,
    inputs="my_salutation",
    outputs="my_message",
    name="join_statements_node"
)