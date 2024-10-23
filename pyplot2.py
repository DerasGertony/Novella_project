from ld_images import *

text2 = {
    (2, 0, 0): "Время на часах: 22:00.",

    (2, 0, 1): "Вы чувствуете себя так, будто не спали несколько лет. "
               "От проведенных нескольких часов подряд за дз у вас начала кружиться голова. ",

    (2, 0, 2): "В последнее время вы даже стали видеть странные сны, где приходите в деканат и пишите заявление об отчислении. ",

    (2, 0, 3): "Почти все ваше свободное время проходит за учебой, но вы все равно ничего не успеваете. "
               "Навязчивые видения того, как вы в будущем собираете милостыню на вокзале, стали появляться все чаще. ",

    (2, 0, 4): "Из этого угнетающего потока мыслей вас вырывает внезапный телефонный звонок. ",

    (2, 0, 5): "Вам звонит ваш староста.",

    (2, 0, 6): "Мигом вас накрывает волна беспокойства.",

    (2, 0, 7): "Быть может, он звонит, чтобы сказать о том, что у вас незачет по матанализу? "
               "Или вас уже собираются отчислить? ",

    (2, 0, 8): "Однако приняв любой неприятный исход, вы берете трубку.",

    (2, 0, 9): "(ваня) - Привет! У меня к тебе предложение, от которого ты не в силах отказаться.",

    (2, 0, 10): "В вас растет любопытство. Пожалуй, на самом деле все не так плохо, как вы думали.",

    (2, 0, 11): "(гг) - Привет, я слушаю.",

    (2, 0, 12): "(ваня) - Не хочешь сходить выпить прямо сейчас? Сегодня такой замечательный праздник! Я уверен, его стоит отметить.",

    (2, 0, 13): "(гг) - И какой же праздник?",

    (2, 0, 14): "(ваня) - День микроволновки.",

    (2, 0, 15): "(гг) - Замечательный, согласен. ",

    (2, 0, 16): "(ваня) - Слушай, нам ведь стоит отдыхать хоть иногда. Не отказывайся!",

    (2, 1, 0): "(гг) - Ладно, ты прав. Скоро выйду.",

    (2, 1, 1): "Отдыхать правда стоит. Особенно в такие моменты. Даже несмотря на то, что завтра целых 3 семинара.",

    (2, 1, 2): "Да ладно, когда не выкручивались? ",

    (2, 1, 3): "Вы быстро собрались и вышли из дома.",

    (2, 1, 4): "2 часа ночи.",

    (2, 1, 5): "Вы только что вернулись домой.",

    (2, 1, 6): "Голова все еще немного кружится. Однако вы чувствуете себя невероятно бодрым и энергичным. ",

    (2, 1, 7): "У вас появляется непреодолимое желание провести остаток ночи продуктивно. "
               "Вы как раз вспомнили о недоделанном дз по дискретной математике. ",

    (2, 1, 8): "По списку вас должны завтра вызвать к доске самым первым, поэтому имеет смысл разобраться в теме. "
               "Все же вы не хотите позориться перед всей группой. ",

    (2, 1, 9): "Однако неизвестно, надолго ли хватит у вас энергии сидеть еще несколько часов за дз.",

    (2, 2, 0): "В предвкушении продуктивного времяпрепровождения вы открыли четвертую банку энергетика. ",

    (2, 2, 1): "Выпив немного, вы сразу же принялись за работу. ",

    (2, 2, 2): "Время на часах: 5:00. ",

    (2, 2, 3): "Вы наконец закончили. ",

    (2, 2, 4): "Спать осталось совсем немного, но вы хотя бы остались довольны проделанной работой и своими усилиями.",

    (2, 2, 5): "Однако от прилива энергии не осталось ни следа. Вы чувствуете себя выжатой тряпкой. ",

    (2, 2, 6): "Абсолютно без сил вы поплелись к кровати и мгновенно рухнули на нее так, будто вас подстрелили. ",

    (2, 2, 7): "Сон полностью поглотил ваше сознание почти моментально.",

    (2, 2, 8): "Вам невероятно спокойно и хорошо. "
               "Однако ваше блаженство прерывает крайне неприятный звук, который становится с каждой секундой все громче и громче.",

    (2, 2, 9): "Вы были готовы отдать все, чтобы побыть в этом приятном небытие хотя бы еще 5 минут, "
               "но раздражающий звук звонка настойчиво пытался вернуть вас в мрачную реальность.",

    (2, 2, 10): "Вы окончательно просыпаетесь и раздраженно берете телефон в руки. ",

    (2, 2, 11): "Вам звонист староста.",

    (2, 2, 12): "(ваньк) - Доброе утро! Спишь?",

    (2, 2, 13): "(гг) - Вообще-то сплю.",

    (2, 2, 14): "(ваньк) - Отлично, как раз собирался тебя разбудить. Боялся, что ты проспишь.",

    (2, 2, 15): "Ладно, увидимся!",

    (2, 2, 16): "Ваше раздражение ушло и сменилось на благодарность старосте. ",

    (2, 2, 17): "Вы уверены, что вам сильно повезло с ним, ведь не в каждой группе есть такой золотой человек.",

    (2, 2, 18): "Вы неохотно встали с кровати. ",

    (2, 2, 19): "После вчерашней прогулки со старостой у вас болела голова. "
                "Несмотря на это, в целом вы чувствовали себя довольно хорошо. ",

    (2, 2, 20): "Вы спокойно собрались, а затем вышли из дома. ",

    (2, 2, 21): "За несколько минут вы дошли до остановки.",

    (2, 2, 22): "Как только вы добрались до нее, то увидели сразу же два остановившихся автобуса - 90ый и 9ый. 90ый, "
                "как правило, едет довольно быстро, но в этот раз он был полностью забитым. 9ый же, наоборот, был практически пустым. ",

    (2, 2, 23): "Однако вы совершенно не знали ни его маршрут, ни сколько примерно может занять дорога на нем.",

    (2, 3, 0): "Вы решили не рисковать и сесть на автобус с знакомым маршрутом, "
               "приняв тот факт, что придется потерпеть эту обыкновенную утреннюю давку. ",

    (2, 3, 1): "Вы с трудом протиснулись в автобус, "
               "растолкав людей и услышав после этого раздраженные вздохи и не очень приятные выражения в свою сторону. ",

    (2, 3, 2): "Находиться в этом адском котле было как физически, так и морально тяжело, но вы уже сделали выбор, пути назад нет. ",

    (2, 3, 3): "Вы решили, что необходимо каким-то образом отвлечь себя, чтобы время, проведенное здесь, прошло как будто бы быстрее. ",

    (2, 4, 0): "Вы увидели квадроберов - переодетых в животных детей, на которых обратили внимание и остальные пассажиры.",

    (2, 4, 1): "Послышались недовольные вздохи и возгласы.",

    (2, 4, 2): "(бабка 1): - Ну и срам! Что за дети пошли!",

    (2, 4, 3): "Слова негодующей пенсионерки моментально нашли свой отклик в толпе.",

    (2, 4, 4): "Да уж, в наше время такого не было! ",

    (2, 4, 5): "Началось бурное обсуждение. ",

    (2, 4, 6): "Среди ворчливых голосов и звуков послышался голос очередной бабушки, яростно желающей высказать свое ценное мнение.",

    (2, 4, 7): "(бабка2) - Че раскудахтались на деток то, как курицы в курятнике? ",

    (2, 4, 8): "Вам бы за собой смотреть!",

    (2, 4, 9): "(бабка1) - А ты сама то не хами, хабалка! Вот из-за тебе подобных такое поколение и вырастает!",

    (2, 4, 10): "Толпа активно зашумела. ",

    (2, 4, 11): "Весь автобус разразился ворчанием, криками негодования и весьма оскорбительными словами. ",

    (2, 4, 12): "В порыве обиды и злости одна из пенсионерок начала бить тростью другую участницу скандала. "
                "Шокированные и взбешенные пассажиры начали толкаться, превратив и так забитый автобус в настоящий ад. "
                "От громких криков и людей, толкающих вас из стороны в сторону, будто бы собираясь разодрать вас на части, "
                "вам стало плохо. ",

    (2, 4, 13): "Вас накрыла удушающе неприятная слабость, у вас закружилась голова, потемнело в глазах. ",

    (2, 4, 14): "Почувствовав, что пора бы выбираться из давки как можно скорее, иначе окружающие заклюют вас здесь, "
                "как голодные вороны, вы попытались пройти ближе к выходу.",

    (2, 4, 15): "Несмотря на то, что двери находились не так далеко, вы сто раз пожалели о попытке протиснуться вперед. "
                "Вас несколько раз ударили локтями по лицу, а затем зажали в углу. ",

    (2, 4, 16): "К тому моменту силы стали окончательно покидать вас. "
                "Кислород будто бы совсем пропал из автобуса, вам стало невозможно дышать.",

    (2, 4, 17): "Черная пелена начала появляться перед глазами. ",

    (2, 4, 18): "Звуки становились все тише. ",

    (2, 4, 19): "Вы больше не чувствовали собственное тело. ",

    (2, 4, 20): "Дискомфорт окончательно пропал. ",

    (2, 4, 21): "Кто бы мог подумать, что вас настигнет именно такой конец... ",

    (2, 5, 0): "В такой давке вы еле как смогли достать телефон из кармана. "
               "Вы залипли в нем, совсем не следя за временем. ",

    (2, 5, 1): "Вы были уверены, что сразу поймете, где выходить, поэтому особо не волновались по этому поводу.",

    (2, 5, 2): "Переписка с друзьями была уж слишком увлекательной и явно затянула вас надолго.",

    (2, 5, 3): "Так надолго, что, оторвавшись от телефона и посмотрев в окно, вы увидели аэропорт. ",

    (2, 5, 4): "В вашей голове царило полное непонимание происходящего. ",

    (2, 5, 5): "90ый, вроде как, не ходит до аэропорта?",

    (2, 5, 6): "Нет, вы определенно что-то путаете. ",

    (2, 5, 7): "Долго не задумываясь о том, как подобное паранормальное явление вообще могло произойти, вы вышли из автобуса. ",

    (2, 5, 8): "Вам показалось, что сейчас, возможно, решается ваша судьба. "
               "И от вашего решения зависит вся ваша дальнейшая жизнь. ",

    (2, 5, 9): "Вдруг такой возможности больше не будет? ",

    (2, 5, 10): "Может это намек от Вселенной? ",

    (2, 5, 11): "Нет, точно надо что-то делать с этим. Такие вещи просто так не случаются.",

    (2, 6, 0): "Вы решили, что пора наконец менять свою жизнь.",

    (2, 6, 1): "Вы купили билеты на Мальдивы в один конец на абсолютно все свои деньги.",

    (2, 6, 2): "Вы улетели туда без единой копейки, но так как вы были на Мальдивах, это не имело никакого для вас значения.",

    (2, 6, 3): "Вы прожили счастливую жизнь.",

    (2, 7, 0): "Вы решили не принимать никаких необдуманных решений. ",

    (2, 7, 1): "Все, что вам сейчас нужно - добраться до университета и прийти на пары. "
               "Хотя бы на последнюю вы обязаны успеть. ",

    (2, 7, 2): "Вы сели на остановке и стали ждать автобус.",

    (2, 7, 3): "Через какое-то время вы наконец добрались до корпуса. Уже как 30 минут шла последняя пара. ",

    (2, 7, 4): "Тем не менее вы решились зайти, ведь не зря столько времени потратили на дорогу. ",

    (2, 7, 5): "Однако в ту же секунду вы пожалели о своем решении. "
               "Вы совсем забыли о том, что в этот день должна быть контрольная по матанализу. ",

    (2, 7, 6): "Мало того, что вы пропустили значительную часть от нее, так и еще и преподаватель встретил вас с не очень дружелюбным выражением лица. ",

    (2, 7, 7): "Про автомат вы точно можете забыть до конца 4 курса.",

    (2, 8, 0): "Вы решили отдать приоритет собственному комфорту. "
               "Все же не всегда выпадает возможность занять место в автобусе, особенно утром. ",

    (2, 8, 1): "Абсолютно довольный своей жизнью вы сидели в автобусе, пока не решили через какое-то время выглянуть в окно. ",

    (2, 8, 2): "Вид за окном становился все более угнетающим. ",

    (2, 8, 3): "Ваше приподнятое настроение, соответственно, сменилось на некую настороженность. Беспокойство охватило вас. Вы видите этот мрачный район впервые. ",

    (2, 8, 4): "Видимо, вы сели не в тот автобус. ",

    (2, 8, 5): "Вы поторопились тут же покинуть его. Выйдя на остановку, вы оглянулись вокруг, пытаясь определить, что это за место. "
               "В конце концов осознание того, где вы находитесь, вселило в вас ужас. ",

    (2, 8, 6): "Сортировка.",

    (2, 8, 7): "Как известно, люди отсюда не возвращаются.",

    (2, 9, 0): "Раз вы решили отдохнуть, то отдыхать нужно до конца. ",

    (2, 9, 1): "У вас будет еще время разобраться с темой позже.",

    (2, 9, 2): "К тому же, если вы совершенно не выспитесь, какая будет от этого польза? ",

    (2, 9, 3): "Маловероятно, что вы сможете адекватно решить что-то, даже если пройдетесь по этой теме вдоль и поперек. ",

    (2, 9, 4): "Тем более за этот тяжелый день вы и так сделали довольно много. ",

    (2, 9, 5): "Считая, что вы определенно заслужили здоровый сон, вы со спокойной душой легли спать.",

    (2, 9, 6): "Будильник разбудил вас. ",

    (2, 9, 7): "К счастью, вы проснулись вовремя. ",

    (2, 9, 8): "После вчерашней прогулки со старостой у вас болела голова. Несмотря на это, в целом вы чувствовали себя довольно хорошо.",

    (2, 9, 9): "Вы спокойно собрались, а затем вышли из дома.",

    (2, 10, 0): "За несколько минут вы дошли до остановки. ",

    (2, 10, 1): "Как только вы добрались до нее, то увидели сразу же два остановившихся автобуса - 90ый и 9ый. ",

    (2, 10, 2): "90ый, как правило, едет довольно быстро, но в этот раз он был полностью забитым. 9ый же, наоборот, был практически пустым. "
                "Однако вы совершенно не знали ни его маршрут, ни сколько примерно он едет. ",

    (2, 11, 0): "Вы решили не рисковать и сесть на автобус с знакомым маршрутом, "
                "приняв тот факт, что придется потерпеть эту обыкновенную утреннюю давку. ",

    (2, 11, 1): "Вы с трудом протиснулись в автобус, "
                "растолкав людей и услышав после этого раздраженные вздохи и не очень приятные выражения в свою сторону. ",

    (2, 11, 2): "Находиться в этом адском котле было как физически, так и морально тяжело, но вы уже сделали выбор, пути назад нет. ",

    (2, 11, 3): "Вы решили, что необходимо каким-то образом отвлечь себя, чтобы время, проведенное здесь, прошло как будто бы быстрее. ",

    (2, 12, 0): "Вы увидели квадроберов - переодетых в животных детей, на которых обратили внимание и остальные пассажиры.",

    (2, 12, 1): "Послышались недовольные вздохи и возгласы.",

    (2, 12, 2): "(бабка 1): - Ну и срам! Что за дети пошли!",

    (2, 12, 3): "Слова негодующей пенсионерки моментально нашли свой отклик в толпе.",

    (2, 12, 4): "Да уж, в наше время такого не было! ",

    (2, 12, 5): "Началось бурное обсуждение. ",

    (2, 12, 6): "Среди ворчливых голосов и звуков послышался голос очередной бабушки, яростно желающей высказать свое ценное мнение.",

    (2, 12, 7): "(бабка2) - Че раскудахтались на деток то, как курицы в курятнике? ",

    (2, 12, 8): "Вам бы за собой смотреть!",

    (2, 12, 9): "(бабка1) - А ты сама то не хами, хабалка! Вот из-за тебе подобных такое поколение и вырастает!",

    (2, 12, 10): "Толпа активно зашумела. ",

    (2, 12, 11): "Весь автобус разразился ворчанием, криками негодования и весьма оскорбительными словами. ",

    (2, 12, 12): "В порыве обиды и злости одна из пенсионерок начала бить тростью другую участницу скандала. "
                 "Шокированные и взбешенные пассажиры начали толкаться, превратив и так забитый автобус в настоящий ад. "
                 "От громких криков и людей, толкающих вас из стороны в сторону, будто бы собираясь разодрать вас на части, "
                 "вам стало плохо. ",

    (2, 12, 13): "Вас накрыла удушающе неприятная слабость, у вас закружилась голова, потемнело в глазах. ",

    (2, 12, 14): "Почувствовав, что пора бы выбираться из давки как можно скорее, иначе окружающие заклюют вас здесь, "
                 "как голодные вороны, вы попытались пройти ближе к выходу.",

    (2, 12, 15): "Несмотря на то, что двери находились не так далеко, вы сто раз пожалели о попытке протиснуться вперед. "
                 "Вас несколько раз ударили локтями по лицу, а затем зажали в углу. ",

    (2, 12, 16): "К тому моменту силы стали окончательно покидать вас. "
                 "Кислород будто бы совсем пропал из автобуса, вам стало невозможно дышать.",

    (2, 12, 17): "Черная пелена начала появляться перед глазами. ",

    (2, 12, 18): "Звуки становились все тише. ",

    (2, 12, 19): "Вы больше не чувствовали собственное тело. ",

    (2, 12, 20): "Дискомфорт окончательно пропал. ",

    (2, 12, 21): "Кто бы мог подумать, что вас настигнет именно такой конец... ",

    (2, 13, 0): "В такой давке вы еле как смогли достать телефон из кармана. "
                "Вы залипли в нем, совсем не следя за временем. ",

    (2, 13, 1): "Вы были уверены, что сразу поймете, где выходить, поэтому особо не волновались по этому поводу.",

    (2, 13, 2): "Переписка с друзьями была уж слишком увлекательной и явно затянула вас надолго.",

    (2, 13, 3): "Так надолго, что, оторвавшись от телефона и посмотрев в окно, вы увидели аэропорт. ",

    (2, 13, 4): "В вашей голове царило полное непонимание происходящего. ",

    (2, 13, 5): "90ый, вроде как, не ходит до аэропорта?",

    (2, 13, 6): "Нет, вы определенно что-то путаете. ",

    (2, 13, 7): "Долго не задумываясь о том, как подобное паранормальное явление вообще могло произойти, вы вышли из автобуса. ",

    (2, 13, 8): "Вам показалось, что сейчас, возможно, решается ваша судьба. "
                "И от вашего решения зависит вся ваша дальнейшая жизнь. ",

    (2, 13, 9): "Вдруг такой возможности больше не будет? ",

    (2, 13, 10): "Может это намек от Вселенной? ",

    (2, 13, 11): "Нет, точно надо что-то делать с этим. Такие вещи просто так не случаются.",

    (2, 14, 0): "Вы решили, что пора наконец менять свою жизнь.",

    (2, 14, 1): "Вы купили билеты на Мальдивы в один конец на абсолютно все свои деньги.",

    (2, 14, 2): "Вы улетели туда без единой копейки, но так как вы были на Мальдивах, это не имело никакого для вас значения.",

    (2, 14, 3): "Вы прожили счастливую жизнь.",

    (2, 15, 0): "Вы решили не принимать никаких необдуманных решений. ",

    (2, 15, 1): "Все, что вам сейчас нужно - добраться до университета и прийти на пары. "
                "Хотя бы на последнюю вы обязаны успеть. ",

    (2, 15, 2): "Вы сели на остановке и стали ждать автобус.",

    (2, 15, 3): "Через какое-то время вы наконец добрались до корпуса. Уже как 30 минут шла последняя пара. ",

    (2, 15, 4): "Тем не менее вы решились зайти, ведь не зря столько времени потратили на дорогу. ",

    (2, 15, 5): "Однако в ту же секунду вы пожалели о своем решении. "
                "Вы совсем забыли о том, что в этот день должна быть контрольная по матанализу. ",

    (2, 15, 6): "Мало того, что вы пропустили значительную часть от нее, так и еще и преподаватель встретил вас с не очень дружелюбным выражением лица. ",

    (2, 15, 7): "Про автомат вы точно можете забыть до конца 4 курса.",

    (2, 16, 0): "Вы решили отдать приоритет собственному комфорту. "
                "Все же не всегда выпадает возможность занять место в автобусе, особенно утром. ",

    (2, 16, 1): "Абсолютно довольный своей жизнью вы сидели в автобусе, пока не решили через какое-то время выглянуть в окно. ",

    (2, 16, 2): "Вид за окном становился все более угнетающим. ",

    (2, 16, 3): "Ваше приподнятое настроение, соответственно, сменилось на некую настороженность. Беспокойство охватило вас. Вы видите этот мрачный район впервые. ",

    (2, 16, 4): "Видимо, вы сели не в тот автобус. ",

    (2, 16, 5): "Вы поторопились тут же покинуть его. Выйдя на остановку, вы оглянулись вокруг, пытаясь определить, что это за место. "
                "В конце концов осознание того, где вы находитесь, вселило в вас ужас. ",

    (2, 16, 6): "Сортировка.",

    (2, 16, 7): "Как известно, люди отсюда не возвращаются.",

    (2, 17, 0): "Вы без происшествий добрались до станции метро и доехали до одной из остановок на Автозаводе. ",

    (2, 17, 1): "Времени до пары оставалось еще достаточно, поэтому у вас промелькнула мысль о том, почему бы не пройтись пешком до корпуса. ",

    (2, 18, 0): "Выйдя из автобуса, вы столкнулись с гопниками.",

    (2, 18, 1): "(гопота) - Э, слышь, зажигалка не найдется?",

    (2, 19, 0): "Вы решили не рисковать, потому что, очевидно, хотите вернуться живым после пар. А таких людей лучше не злить.",

    (2, 19, 1): "] (гг) - Да, конечно, держите...",

    (2, 19, 2): "(гопота) - Спасибо, брат. В долгу не останемся. Че, тя подвезти надо?",

    (2, 19, 3): "(гг) - Да нет, спасибо. Мне тут пешком минут 15..",

    (2, 19, 4): "(гопота) - Да не кипишуй ты, залазь в тачку. Че как не родной, а?",

    (2, 19, 5): "Вы беспрекословно сделали то, о чем вас попросили . ",

    (2, 19, 6): "Гопникам понравилась ваша выдержка.",

    (2, 19, 7): "Вы стали новым авторитетом на Автозаводе, теперь под вами ходит весь район.",

    (2, 20, 0): "(гг) - Нет, извините, я не курю.",

    (2, 20, 1): "Выражение лиц у всей толпы изменилось на крайне раздраженное. ",

    (2, 20, 2): "Они выглядели, как стая орлов, готовых налететь на свою жертву и разорвать ее в клочья.",

    (2, 20, 3): "(гопота) - Еще раз, для особо одаренных спрашиваю, зажигалки не найдется?",

    (2, 20, 4): "Вы чувствовали себя так, будто вас загнали в одну клетку с голодными тиграми. ",

    (2, 20, 5): "Вы пятились назад, но гопники все приближались к вам.",

    (2, 20, 6): "(гг) - Н-нет, говорю же, я...",

    (2, 20, 7): "Вы не успели договорить, так как вам внезапно прилетело по лицу настолько сильно, "
                "что в глазах начало стремительно темнеть. ",

    (2, 20, 8): "Почти сразу же вы упали без сознания.",

    (2, 20, 9): "Вы проснулись в больнице с многочисленными травмами. "
                "Очевидно, что пары пришлось пропустить. ",

    (2, 20, 10): "Что ж, очевидно, что автомат вам больше не светит...",

    (2, 21, 0): "Времени до начала пары было достаточно. Вы шли какое-то время, любуясь видами прекрасного Автозавода. ",

    (2, 21, 1): "Внезапно впереди показалась знакомая фигура. ",

    (2, 21, 2): "Подойдя ближе, вы узнали Бориса Игоревича. ",

    (2, 21, 3): "(БИ)- Доброе утро, студент. ",

    (2, 21, 4): "У меня к вам замечательное предложение. ",

    (2, 21, 5): "Не хотели бы вы сходить со мной поесть шаурму? ",

    (2, 21, 6): "(гг) - Здравствуйте, Борис Игоревич. ",

    (2, 21, 7): "К сожалению, у меня скоро начнется пара... ",

    (2, 21, 8): "Я даже не знаю, что ответить...",

    (2, 21, 9): "Ваш академический руководитель, кажется, выглядел расстроенным.",

    (2, 22, 0): "(гг) - Хорошо, я согласен.",

    (2, 22, 1): "Борис Игоревич был крайне доволен вашим ответом.",

    (2, 22, 2): "Вы пропустили первую пару, но зато насладились прекрасной компанией и шаурмой. ",

    (2, 22, 3): "Кстати, у вас автомат по всем предметам.",

    (2, 23, 0): "(гг) - Извините, вынужден отказать. Иначе я опоздаю на пару.",

    (2, 23, 1): "На самом деле, это было не просто предложение поесть шаурму. ",

    (2, 23, 2): "Это был зачет по ТП. ",

    (2, 23, 3): "Вы не прошли его и, к сожалению, вас отчислили...",

    (2, 24, 0): "(гг) - Нет, извини. ",

    (2, 24, 1): "У меня еще куча долгов, лучше разберусь с ними.",

    (2, 24, 2): "Как нибудь в другой раз.",

    (2, 24, 3): "(ванютикс) - Зря отказываешься. ",

    (2, 24, 4): "Ну, как скажешь.",

    (2, 24, 5): "Пока...",

    (2, 24, 6): "Вы кладете трубку, пытаясь отогнать мысли о том, "
                "что пропустили такой прекрасный шанс наконец сбежать от надоедающей рутины. ",

    (2, 24, 7): "Хотя отдыхать, конечно, полезно, но кто тогда закроет за вас все долги? ",

    (2, 24, 8): "У вас еще будет полно времени на отдых. ",

    (2, 24, 9): "Когда-нибудь. ",

    (2, 24, 10): "Не обязательно в следующей жизни.",

    (2, 24, 11): "Вы как раз вспомнили о недоделанном дз по дискретной математике. ",

    (2, 24, 12): "По списку вас должны завтра вызвать к доске самым первым, поэтому стоит разобраться в теме. "
                 "Все же вы не хотите позориться перед всей группой. ",

    (2, 24, 13): "Однако силы как на зло начали покидать вас. [2, 24, 14]Вы бросили взгляд на кровать. ",

    (2, 24, 14): "Вы бросили взгляд на кровать. ",

    (2, 24, 15): "Она так и манила вас к себе, как бы вы не пытались сдерживаться.",

    (2, 24, 16): "Держать глаза открытыми уже давалось вам с трудом. ",

    (2, 24, 17): "Вы уже были готовы уснуть даже за письменным столом. ",

    (2, 25, 0): "Несчастно вздохнув, вы открыли четвертую банку энергетика. ",

    (2, 25, 1): "Выпив немного, вы сразу же принялись за работу. ",

    (2, 25, 2): "3 часа ночи. ",

    (2, 25, 3): "Вы наконец закончили. ",

    (2, 25, 4): "Спать осталось совсем немного, но вы хотя бы остались довольны проделанной работой и своими усилиями. ",

    (2, 25, 5): "Вы чувствуете себя выжатой тряпкой. ",

    (2, 25, 6): "Абсолютно без сил вы поплелись к кровати и мгновенно рухнули на нее так, будто вас подстрелили. "
                "Сон полностью поглотил ваше сознание почти моментально.",

    (2, 25, 7): "Сон длился подозрительно долго. ",

    (2, 25, 8): "Несмотря на то, как хорошо вам было, что-то глубоко в сознании заставило вас проснуться. "
                "И не зря. "
                "Первым делом вы полезли в телефон смотреть время. ",

    (2, 25, 9): "К несчастью вы обнаружили, что очень сильно опаздываете.",

    (2, 25, 10): "Дело в том, что вы совсем забыли поставить будильник из-за невыносимой усталости, когда ложились спать. ",

    (2, 25, 11): "Вы резко схватили банку с энергетиком и быстро допили его. "
                 "Прилив энергии позволил собраться вам, не потратив на это много времени. ",

    (2, 25, 12): "Очевидно, что завтраком пришлось пожертвовать. ",

    (2, 25, 13): "Вы снова взглянули на время и поняли, что на автобусе с пересадкой вам никак не добраться до начала пары. ",

    (2, 25, 14): "Единственный выход, если вы хотите получить автомат у Киры Владимировны, - заказать такси до самого корпуса. "
                 "Однако проблема в том, что вы студент. ",

    (2, 25, 15): "Бедный студент. ",

    (2, 25, 16): "Такие расходы, как правило, для вас непозволительны, но сейчас ситуация действительно критичная.",

    (2, 26, 0): "Вы были уверены, что автомат того стоит, ведь такси за считанные минуты довезло вас до корпуса.",

    (2, 26, 1): "Но стоит ли оно голодовки целый месяц? ",

    (2, 26, 2): "Теперь придется что-то предпринимать, если вы хотите выжить. ",

    (2, 26, 3): "Чем раньше вы примите решение, тем будет лучше, ведь голодный человек способен на многие вещи, не всегда позволительные.",

    (2, 27, 0): "Временное унижение явно лучше, чем голодная смерть. "
                "Вы стали просить милостыню рядом с ВУЗом. ",

    (2, 27, 1): "К счастью, нашлись отзывчивые люди, которые помогли вам.",

    (2, 27, 2): "Вы смогли накопить на чокопай.",

    (2, 28, 0): "Ваша гордость не позволила вам слезно выпрашивать у прохожих деньги.",

    (2, 28, 1): "Вы пошли на пары. ",

    (2, 28, 2): "Чем голоднее вы становились, тем сложнее было сохранять ясность рассудка. "
                "В итоге естественная потребность победила все ваши принципы и нравственные установки. ",

    (2, 28, 3): "Вы съели одногруппника прямо на паре. За такой проступок вас отчислили.",

    (2, 29, 0): "Вы решили, что автомат по дискретке не настолько уж важен для вас, чтобы целый месяц голодать из-за него. ",

    (2, 29, 1): "К сожалению, вы не успели приехать на пару вовремя.",

}

btn2 = {
    (2, 0, 1): ["Да", (2, 1, 0)],
    (2, 1, 1): ["Начать делать дискретку - Лох", (2, 2, 0)],
    (2, 2, 1): ["90", (2, 3, 0)],
    (2, 3, 1): ["Смотреть в окно", (2, 4, 0)],
    (2, 3, 2): ["Залипнуть в телефоне", (2, 5, 0)],
    (2, 5, 1): ["Купить билеты на Мальдивы", (2, 6, 0)],
    (2, 5, 2): ["Поехать на пару по матанализу", (2, 7, 0)],
    (2, 2, 2): ["9", (2, 8, 0)],
    (2, 1, 2): ["Пойти спать - Сигма", (2, 9, 0)],
    (2, 9, 1): ["Автобус", (2, 10, 0)],
    (2, 10, 1): ["90", (2, 11, 0)],
    (2, 11, 1): ["Смотреть в окно", (2, 12, 0)],
    (2, 11, 2): ["Залипнуть в телефоне", (2, 13, 0)],
    (2, 13, 1): ["Купить билеты на Мальдивы - Сигма", (2, 14, 0)],
    (2, 13, 2): ["Поехать на пару по матанализу", (2, 15, 0)],
    (2, 10, 2): ["9", (2, 16, 0)],
    (2, 9, 2): ["Метро", (2, 17, 0)],
    (2, 17, 1): ["Автобус", (2, 18, 0)],
    (2, 18, 1): ["Да", (2, 19, 0)],
    (2, 18, 2): ["Нет", (2, 20, 0)],
    (2, 17, 2): ["Пешком", (2, 21, 0)],
    (2, 21, 1): ["Принять предложение Бориса Игоревича", (2, 22, 0)],
    (2, 21, 2): ["Отказаться от предложения", (2, 23, 0)],
    (2, 0, 2): ["Нет", (2, 24, 0)],
    (2, 24, 1): ["Начать делать дискру", (2, 25, 0)],
    (2, 25, 1): ["Да", (2, 26, 0)],
    (2, 26, 1): ["Да", (2, 27, 0)],
    (2, 26, 2): ["Нет", (2, 28, 0)],
    (2, 25, 2): ["Нет", (2, 29, 0)]

}

mx2 = {
    (2, 0): 16,
    (2, 1): 9,
    (2, 2): 23,
    (2, 3): 3,
    (2, 4): 21,
    (2, 5): 11,
    (2, 6): 3,
    (2, 7): 7,
    (2, 8): 7,
    (2, 9): 9,
    (2, 10): 2,
    (2, 11): 3,
    (2, 12): 21,
    (2, 13): 11,
    (2, 14): 3,
    (2, 15): 7,
    (2, 16): 7,
    (2, 17): 1,
    (2, 18): 1,
    (2, 19): 7,
    (2, 20): 10,
    (2, 21): 9,
    (2, 22): 3,
    (2, 23): 3,
    (2, 24): 17,
    (2, 25): 16,
    (2, 26): 3,
    (2, 27): 2,
    (2, 28): 3,
    (2, 29): 1

}

hero2 = {

    (2, 0, 9): biv_ild,
    (2, 0, 12): biv_ild,
    (2, 0, 14): biv_ild,
    (2, 0, 16): biv_ild,
    (2, 2, 12): biv_ild,
    (2, 2, 14): biv_ild,
    (2, 2, 15): biv_ild,
    (2, 4, 2): gm_angry,
    (2, 4, 4): gm_angry,
    (2, 4, 7): gm_good,
    (2, 4, 8): gm_good,
    (2, 4, 9): gm_angry,
    (2, 12, 2): gm_angry,
    (2, 12, 4): gm_angry,
    (2, 12, 7): gm_good,
    (2, 12, 8): gm_good,
    (2, 12, 9): gm_angry,
    (2, 18, 1): [gop_normal1, gop_normal2],
    (2, 19, 2): [gop_friendly1, gop_friendly2],
    (2, 19, 4): [gop_friendly1, gop_friendly2],
    (2, 20, 3): [gop_normal1, gop_normal2],
    (2, 21, 3): bi_sigma,
    (2, 21, 4): bi_sigma,
    (2, 21, 5): bi_sigma,
    (2, 24, 3): biv_ild,
    (2, 24, 4): biv_ild,
    (2, 24, 5): biv_ild,
}

back2 = {}

WinOrLose2 = {
    (2, 3, 21) : 0,
    (2, 6, 3): 1,
    (2, 7, 7): 0,
    (2, 8, 7): 0,
    (2, 12, 21): 0,
    (2, 14, 3): 1,
    (2, 15, 7): 0,
    (2, 16, 7): 0,
    (2, 19, 7): 1,
    (2, 20, 9): 0,
    (2, 22, 3): 1,
    (2, 23, 3): 0,
    (2, 27, 2): 1,
    (2, 28, 3): 0,
    (2, 29, 1): 0
}

TimeSkip2 = {
    (2, 1, 3): 1,
    (2, 2, 1): 1,
    (2, 2, 7): 1,
    (2, 5, 1): 1,
    (2, 7, 2): 1,
    (2, 9, 5): 1,
    (2, 13, 1): 1,
    (2, 15, 2): 1,
    (2, 20, 7): 1,
    (2, 25, 1): 1,
    (2, 25, 6): 1,
}