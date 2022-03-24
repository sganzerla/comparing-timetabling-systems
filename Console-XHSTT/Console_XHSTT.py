import xml.etree.ElementTree as ET

# http://jeffreykingston.id.au/khe/
instances_khe = [
    "./instances/KHE/2014_08_19_KHE14x8_solns.xml",    
    "./instances/KHE/AU-BG-98_soln.xml", 
    "./instances/KHE/AU-BG-98_soln2.xml", 
    "./instances/KHE/2014_08_19_KHE14x8_solns.xml", 
    "./instances/KHE/khe14_solns.xml"
    ]

# https://www.utwente.nl/en/eemcs/dmmp/hstt/datasets/
instances_tu = [
    "./instances/twente-university/BrazilInstance2.xml",
    "./instances/twente-university/CzechVillageSchool.xml",
    "./instances/twente-university/DenmarkFalkonergaardensGymnasium2012.xml",
    "./instances/twente-university/ItalyInstance1.xml",
    ]

files = instances_khe + instances_tu
filters = ["Times", "Resources", "Events", "Constraints"]

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return root


def print_child_by_filter(xml_root, filter, print_all=False):
    children = 0
    
    for child in xml_root.iter(filter):
        if print_all:
            print(child.tag, ":", child.attrib)      
           
        children += 1
    print("\nTotal number of", filter, ":", children)
    

def main():
    
    for file in files:
        print("\nFile:", file)
        root = parse_xml(file)
        for filter in filters:
            print_child_by_filter(root, filter)
        print("----------------------------------------------------")


if __name__ == "__main__":
    main()
