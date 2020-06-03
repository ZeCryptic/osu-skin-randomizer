import os
from random import choice
from shutil import copyfile, rmtree

import skin_elements

randomized_skin_name = "!RANDOM"


def randomize(osu_skins_dir_path, rand_hit=True, rand_score=True, rand_judge=True, rand_follow=True):
    if not os.path.exists(osu_skins_dir_path):
        raise Exception("ERROR: Directory does not exist")
    new_skin_path = delete_and_remake_skin(osu_skins_dir_path)  # dir/Skins/{randomized_skin_name}
    add_random_elements_to_new_skin(new_skin_path, osu_skins_dir_path, rand_hit, rand_score, rand_judge, rand_follow)


def get_all_skins_paths(osu_skin_dir_path) -> [str]:
    skins_dir_list = [f'{osu_skin_dir_path}\\{path}' for path in os.listdir(osu_skin_dir_path) if
                      os.path.isdir(f'{osu_skin_dir_path}\\{path}')
                      and path != randomized_skin_name]
    if len(skins_dir_list) < 1:
        raise Exception("ERROR: Not enough skins in directory")
    return skins_dir_list


def delete_and_remake_skin(skin_dir_path) -> str:
    new_skin_path = f'{skin_dir_path}\\{randomized_skin_name}'
    if os.path.exists(new_skin_path):
        rmtree(new_skin_path)
    os.mkdir(new_skin_path)
    return new_skin_path


def add_helper(new_skin_path, osu_skins_dir_path, elements, rand_for_all=True):
    random_skin = choice(get_all_skins_paths(osu_skins_dir_path))
    for element in elements:
        if rand_for_all:
            random_skin = choice(get_all_skins_paths(osu_skins_dir_path))
        new_element_source = f'{random_skin}\\{element}'
        if os.path.exists(new_element_source):
            new_element_destination = f'{new_skin_path}\\{element}'
            copyfile(new_element_source, new_element_destination)


def add_random_elements_to_new_skin(new_skin_path, osu_skins_dir_path, rand_hit, rand_score, rand_judge, rand_follow):
    elements_list_of_lists = skin_elements.elements
    add_helper(new_skin_path, osu_skins_dir_path, elements_list_of_lists[0])
    add_helper(new_skin_path, osu_skins_dir_path, elements_list_of_lists[1], rand_hit)
    add_helper(new_skin_path, osu_skins_dir_path, elements_list_of_lists[2], rand_score)
    add_helper(new_skin_path, osu_skins_dir_path, elements_list_of_lists[3], rand_judge)
    add_helper(new_skin_path, osu_skins_dir_path, elements_list_of_lists[4], rand_follow)
