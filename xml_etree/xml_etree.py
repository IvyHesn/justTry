#!/usr/bin/env python
# -*- coding: gbk -*-
from lxml import etree


def create_tree(file_path):
    tree = etree.parse(file_path)
    return tree

tree = create_tree('items.xml')
root = tree.getroot()


def find_nodelist(tree, Xpath):
    '''
    ���ص��Ƿ����������б�
    '''
    root = tree.getroot()
    nodelist = root.findall(Xpath)
    return nodelist


def find_attrib_value(node, name):
    '''ʹ��find_nodelist()��������Ҫ��һ�����ָ�������Ե�ֵ'''
    value = node.attrib[name]
    return value

# nodelist=find_nodelist(tree,'./levels[@id="0"]/level[@id="0"]/createItems/createElement[@elementId="0"]')
nodelist = find_nodelist(tree, './item[@id="1"]/award')
node = nodelist[0]
node.set('step', '5')
value = find_attrib_value(nodelist[0], 'step')
print(value)


def change_attrib_value(node, key, value):
    '''
    �޸����Ե�ֵ
    '''
    node.set(key, value)


def write_xml(tree, out_path):
    '''��xml�ļ�д��
            tree: xml��
            out_path: д��·��'''
    tree.write(out_path, encoding="utf-8", xml_declaration=True)

#child2= etree.SubElement(root, "child2")
#child3 = etree.SubElement(child2, "child3")

#print (etree.tostring(root,pretty_print=True))


write_xml(tree, 'items2.xml')
