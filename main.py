# University of Notre Dame
# Course CSE 40537 / 60537 - Biometrics - Spring 2020
# Instructor: Daniel Moreira (dhenriq1@nd.edu)
# Fingerprint Recognition
# TODO: Test script. Better description will be added soon.
# Language: Python 3

import a_acquire
import b_enhance
import c_describe
import d_match

# Test script.
# TODO: Better description will be added soon.

total_done = 0
with open("fingerprint_data/genuine.txt") as genuine_pairs, open('output.csv', mode='w') as output_file:
    lines = genuine_pairs.readlines()
    for line in lines:
        line = line.strip()
        split_pair = line.split(",")
        first_print =  split_pair[0]
        second_print =  split_pair[1]
        first_print_path = "fingerprint_data/" + first_print
        second_print_path = "fingerprint_data/" + second_print
        fingerprint_file_path_1 = first_print_path
        fingerprint_file_path_2 = second_print_path

        fingerprint_1 = a_acquire.acquire_from_file(fingerprint_file_path_1, view=False)
        fingerprint_2 = a_acquire.acquire_from_file(fingerprint_file_path_2, view=False)

        pp_fingerprint_1, en_fingerprint_1, mask_1 = b_enhance.enhance(fingerprint_1, dark_ridges=False, view=False)
        pp_fingerprint_2, en_fingerprint_2, mask_2 = b_enhance.enhance(fingerprint_2, dark_ridges=False, view=False)

        ridge_endings_1, bifurcations_1 = c_describe.describe(en_fingerprint_1, mask_1, view=False) #minutiae
        ridge_endings_2, bifurcations_2 = c_describe.describe(en_fingerprint_2, mask_2, view=False)

        matches = d_match.match(en_fingerprint_1, ridge_endings_1, bifurcations_1,
                                en_fingerprint_2, ridge_endings_2, bifurcations_2, view=True)

        print_1_minutiae = len(ridge_endings_1) + len(bifurcations_1)
        print_2_minutiae = len(ridge_endings_2) + len(bifurcations_2)
        total_minutiae = (print_1_minutiae + print_2_minutiae)/2
        total_matches = len(matches[0]) + len(matches[1])
        sim_score = total_matches / total_minutiae

        output_file.write(f'1,{sim_score}\n')
        total_done = total_done + 1
        print(total_done)

    genuine_pairs.close()
    output_file.close()
        
total_done = 0
with open("fingerprint_data/imposter.txt") as imposter_pairs, open('output.csv', mode='w') as output_file:
    lines = genuine_pairs.readlines()
    for line in lines:
        line = line.strip()
        split_pair = line.split(",")
        first_print =  split_pair[0]
        second_print =  split_pair[1]
        first_print_path = "fingerprint_data/" + first_print
        second_print_path = "fingerprint_data/" + second_print
        fingerprint_file_path_1 = first_print_path
        fingerprint_file_path_2 = second_print_path

        fingerprint_1 = a_acquire.acquire_from_file(fingerprint_file_path_1, view=False)
        fingerprint_2 = a_acquire.acquire_from_file(fingerprint_file_path_2, view=False)

        pp_fingerprint_1, en_fingerprint_1, mask_1 = b_enhance.enhance(fingerprint_1, dark_ridges=False, view=False)
        pp_fingerprint_2, en_fingerprint_2, mask_2 = b_enhance.enhance(fingerprint_2, dark_ridges=False, view=False)

        ridge_endings_1, bifurcations_1 = c_describe.describe(en_fingerprint_1, mask_1, view=False) #minutiae
        ridge_endings_2, bifurcations_2 = c_describe.describe(en_fingerprint_2, mask_2, view=False)

        matches = d_match.match(en_fingerprint_1, ridge_endings_1, bifurcations_1,
                                en_fingerprint_2, ridge_endings_2, bifurcations_2, view=True)

        print_1_minutiae = len(ridge_endings_1) + len(bifurcations_1)
        print_2_minutiae = len(ridge_endings_2) + len(bifurcations_2)
        total_minutiae = (print_1_minutiae + print_2_minutiae)/2
        total_matches = len(matches[0]) + len(matches[1])
        sim_score = total_matches / total_minutiae

        output_file.write(f'1,{sim_score}\n')
        total_done = total_done + 1
        print(total_done)

    imposter_pairs.close()
    output_file.close()
