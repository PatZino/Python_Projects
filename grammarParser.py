GRAMMAR = '''
    @@grammar::Calc
    start = E $ ;
    E 
    =
        | sign E
        | digit
        | decimal E
        | decimal
        | E decimal
        | digit E
        | letter E
        | letter
        | E letter
        | digit '*' decimal
        ;
    decimal
    =
        | digit decimal
        | decimal E
        | '.'
        ;
    sign
        =
        | '-'
        | '+'
        ;
    digit = /\d+/ ;
    letter = /\w+/ ;
'''


def main():
    import pprint
    import json
    from tatsu import parse
    from tatsu.util import asjson
    ast = parse(GRAMMAR, '1. 3 ')
    print('PPRINT')
    pprint.pprint(ast, indent=2, width=20)
    print()
    print('JSON')
    print(json.dumps(asjson(ast), indent=2))
    print()


if __name__ == '__main__':
    main()





