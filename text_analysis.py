import os


def word_count(files_folder, list_words):
    result = {}
    list_files = [os.path.join(files_folder, file) for file in os.listdir(files_folder)]
    num_lines = 0

    # Iter through files
    for file_path in list_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            f_lines = f.readlines()
            # Iter through lines
            for line in f_lines:
                num_lines += 1
                # Iter through each word
                for word in list_words:
                    if word in line:
                        count_old = result.get(word, 0)
                        result[word] = count_old + 1

    print(f"Finished -> Through {len(list_files)} files, {num_lines} lines")

    return result


if __name__ == '__main__':
    list_word_countries = ['朝鲜', '美国', '台湾', '巴西', '以色列', '乌克兰', '意大利']
    word_count(files_folder=r"data\news", list_words=list_word_countries)
