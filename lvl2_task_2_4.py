# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

foo1 = "Hi! Hello!"
foo2 = ""
foo3 = "Oh, no!!!"


def remove_exclamation_marks(sp):
    res = []
    result = ''
    for i in sp:
        if i != '!':
            res.append([i])
            result += str(i)
    return(result)

print(remove_exclamation_marks(foo1))
print(remove_exclamation_marks(foo2))
print(remove_exclamation_marks(foo3))
    




# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

foo4 = "Hi!"
foo5 = "Hi!!!"
foo6 = "!Hi"

def remove_last_em(s):

    result = s.rstrip('!')
    return result

print(remove_last_em(foo4))
print(remove_last_em(foo5))
print(remove_last_em(foo6))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    pass