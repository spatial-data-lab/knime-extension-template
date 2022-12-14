# The root category of all {{cookiecutter.extension_name}} categories
import knime_extension as knext

# This defines the root {{cookiecutter.extension_name}} KNIME category that is displayed in the node repository
category = knext.category(
    path="/community",
    level_id="{{cookiecutter.extension_name}}", # this is the id of the category in the node repository #FIXME: 
    name="{{cookiecutter.extension_name}}",
    description="{{cookiecutter.description}}",
    # starting at the root folder of the extension_module parameter in the knime.yml file
    icon="icons/icon/{{cookiecutter.extension_name}}.png",
)


# need import node files here
import nodes.my_nodes_catergery
