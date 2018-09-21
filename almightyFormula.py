GRAMMAR = '''
    @@grammar::Calc
    start = E $ ;
    E 
        =
        | E '^' T
        | T
        ;
    T
        =
        | T '/' F
        | T '*' F
        | T '+' F
        | T '-' F
        | unaryop F
        | F
        ;
    F
        =
        | '('E')'
        | id
        | digit
        ;
    unaryop = /-/;
    id = /\w+/;
    digit = /\d+/ ;
'''


def main(sen):
    import pprint
    import json
    from tatsu import parse
    from tatsu.util import asjson
    # test sen = (-b + ((b * b) - (4 * a * c)) ^ (1/2)) / (2 * a)
    ast = parse(GRAMMAR, sen)
    print('PPRINT')
    pprint.pprint(ast, indent=2, width=20)
    print()
    print('JSON')
    print(json.dumps(asjson(ast), indent=2))
    print()


sentence = input("Enter your expression: ")
if __name__ == '__main__':
    main(sentence)





