GRAMMAR = '''
    @@grammar::Calc
    start = expression $ ;
    expression 
    =
        | term '+' expression
        | term '-' expression
        | term
        ;
    term
    =
        | factor '*' term
        | factor '/' term
        | factor
        ;
    factor
        =
        | '(' expression ')'
        | number
        ;
    number = /\d+/ ;
'''


def main():
    import pprint
    import json
    from tatsu import parse
    from tatsu.util import asjson
    ast = parse(GRAMMAR, '3 + 5 * ( 10 - 20 )')
    print('PPRINT')
    pprint.pprint(ast, indent=2, width=20)
    print()
    print('JSON')
    print(json.dumps(asjson(ast), indent=2))
    print()


if __name__ == '__main__':
    main()





