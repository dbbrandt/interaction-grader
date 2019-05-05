from .Answer import Answer

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

phonemes = [[1,['b', 'bb']],
    [2,['d', 'dd', 'ed']],
    [3,['f','ff','ph','gh','lf','ft']],
    [4,['g','gg','gh','gu','gue']],
    [5,['h','wh']],
    [6,['j','ge','g','dge','di','gg']],
    [7,['k','c','ch','cc','lk','qu'',q(u)','ck','x']],
    [8,['l','ll']],
    [9,['m','mm','mb','mn','lm']],
    [10,['n','nn','kn','gn','pn']],
    [11,['p','pp']],
    [12,['r','rr','wr','rh']],
    [13,['s','ss','c','sc','ps','st','ce','se']],
    [14,['t','tt','th','ed']],
    [15,['v','f','ph','ve']],
    [16,['w','wh','u','o']],
    [17,['z','zz','s','ss','x','ze','se']],
    [18,['s','si','z']],
    [19,['ch','tch','tu','ti','te']],
    [20,['sh','ce','s','ci','si','ch','sci','ti']],
    [21,['ng','n','ngue']],
    [22,['y','i','j']],
    [23,['a','ai','au']],
    [24,['a','ai','eigh','aigh','ay','er','et','ei','au','ea','ey']],
    [25,['e','ea','u','ie','ai','a','eo','ei','ae']],
    [26,['e','ee','ea','y','ey','oe','ie','i','ei','eo','ay']],
    [27,['i','e','o','u','ui','y','ie']],
    [28,['i','y','igh','ie','uy','ye','ai','is','eigh']],
    [29,['a','ho','au','aw','ough']],
    [30,['o','oa','oe','ow','ough','eau','oo','ew']],
    [31,['o','oo','u','ou']],
    [32,['u','o','oo','ou']],
    [33,['o','oo','ew','ue','oe','ough','ui','oew','ou']],
    [34,['oi','oy','uoy']],
    [35,['ow','ou','ough']],
    [36,['a','er','i','ar','our','ur']],
    [37,['air','are','ear','ere','eir','ayer']],
    [38,['ir','er','ur','ear','or','our','yr']],
    [39,['aw','a','or','oor','ore','oar','our','augh','ar','ough','au']],
    [40,['ear','eer','ere','ier']],
    [41,['ure','our']]]

class ShortAnswer(Answer):

    def __init__(self, sentence):
        self.sentence = sentence

