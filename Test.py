from Magic import in_file, out_file
import time


# Данная программа расчитана на конвертацию файла
# расписания дня недели строго схожего фррмата


def main():
    start_time = time.time()
    with open(in_file, "r", encoding="UTF-8") as f:
        line = f.read()
        out_stream = open(out_file, "w", encoding="UTF-8")
        data2 = line.replace("\t", "", line.count("\t"))  # убираю табуляцию и переносы строки
        data2 = line.replace("\n", "", line.count("\n"))
        data = data2.split("<")
        progress = 0
        last_progress = 0
        out_stream.write("{")
        lesson_started = True  # костыль для корретной работы json
        for i in data[1:]:
            i = i.strip()
            tag = i.split(">")[0]
            if "/" not in i:
                progress += 1
                if last_progress == progress:
                    out_stream.write(",\n")
                else:
                    out_stream.write("\n")
                if lesson_started or tag != "lesson":
                    out_stream.write(progress * "\t")
                    out_stream.write(add_quotes(tag) + " : ")
                value = i.split(">")[1]
                if value != "":
                    write_value(add_quotes(value), out_stream)
                else:
                    if tag != "lesson":
                        out_stream.write("{")
                    else:
                        if lesson_started:
                            out_stream.write("[\n" + progress * "\t" + "{")
                            lesson_started = False
                        else:
                            out_stream.write(progress * "\t" + "{")
            else:
                last_progress = progress
                progress -= 1
                if tag == "/lesson":
                    out_stream.write("}")
        out_stream.write("\n" + 2 * "\t" + "]")
        out_stream.write("\n" + "\t" + "}")
        out_stream.write('\n}')
        print(time.time() - start_time)


def write_value(value, file):
    file.write(value)


#  в Python проблема с двойными ковычками, чтобы их хорошо выводить, я сделал функцию
def add_quotes(string):
    return "\"" + string + "\""


if __name__ == "__main__":
    main()
