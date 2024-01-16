def longest_palindromic_length(text):
   n = len(text)
   # 길이가 0인 경우
   if n == 0:
       return 0, ""

   # isps[i][j] : i번째 글자에서 j번째 글자의 부분 문자열이 회문인지 여부를 저장
   isps = [[False] * n for _ in range(n)]
   # longest palindrome length
   lp_length = 1

   # 한 글자 부분 문자열은 항상 회문이다.
   for i in range(n):
       isps[i][i] = True

   # 두 글자 부분 문자열은 두 글자가 같은 경우 회문이다.
   for i in range(n - 1):
       if text[i] == text[i + 1]:
           # 두 글자가 같은 경우 lp_length는 2가 된다.
           isps[i][i + 1] = True
           lp_length = 2

   # 세 글자 이상인 경우, 처음과 끝 글자가 같다면, 이를 제외한 나머지가 회문인지를 확인한다.
   for length in range(3, n + 1):
       for i in range(n - length + 1):
           j = i + length - 1
           # 처음과 끝 글자가 같고, 처음과 끝을 제외한 나머지가 회문인 경우
           if text[i] == text[j] and isps[i + 1][j - 1]:
               isps[i][j] = True
               lp_length = length
   return lp_length

def longest_palindrom(text):
   n = len(text)
   # 길이가 0인 경우
   if n == 0:
       return 0, ""

   # isps[i][j] : i번째 글자에서 j번째 글자의 부분 문자열이 회문인지 여부를 저장
   isps = [[False] * n for _ in range(n)]
   # longest palindrome length
   lp_length = 1

   # 한 글자 부분 문자열은 항상 회문이다.
   for i in range(n):
       isps[i][i] = True

   # 두 글자 부분 문자열은 두 글자가 같은 경우 회문이다.
   for i in range(n - 1):
       if text[i] == text[i + 1]:
           # 두 글자가 같은 경우 lp_length는 2가 된다.
           isps[i][i + 1] = True
           lp_length = 2

   # 세 글자 이상인 경우, 처음과 끝 글자가 같다면, 이를 제외한 나머지가 회문인지를 확인한다.
   for length in range(3, n + 1):
       for i in range(n - length + 1):
           j = i + length - 1
           # 처음과 끝 글자가 같고, 처음과 끝을 제외한 나머지가 회문인 경우
           if text[i] == text[j] and isps[i + 1][j - 1]:
               isps[i][j] = True
               lp_length = length

   # isps를 사용해 회문을 찾는다.
   # 최장 회문의 길이가 1인 경우 빈 리스트를 반환한다.
   if lp_length == 1:
       return lp_length, []

   lp_list = []
   # 최장 회문의 길이를 기준으로 isps[i][i + lp_length - 1]이 True인 경우
   # i번째 글자에서 j번째 글자 까지가 회문이라는 의미이므로
   # text[i:i + lp_length]를 회문 리스트에 추가한다.
   for i in range(n - lp_length + 1):
       j = i + lp_length - 1
       if isps[i][j]:
           lp_list.append(text[i:j + 1])

   return lp_length, lp_list

def main():
    TC1 = 'oavhdjksqw'
    TC2 = 'zveabcdcbacbetrmhhktbslwnzbdwuopihqhhqxmybqgemlscsyzcsxzztacocatpsxzaljbtanshudeogbsdnujkwqwvclojhxbyilwxbyocnguie'
    TC3 = 'cdbbciconpbxbctvdvcjudwytytqleimpemczcawocxuyepgnmkjuhmmpmvlqbwzmwfblrlurwxrjfcdxaktkilnrwxmnfdxpwvwihwkrmbzykxdyrvlqwyffelkdkinhiymzclpxjhafeticmhrfpvbyaxsecytqxnwqhhhvqgnvwtsgskemgkscdurgfjivivkqdhjnnlbyswmzirzxxfgxvbqlxtgjrsiwofovibpxisafyyiwqqlxyiyjqzdbodrfhizaudszsqtpghajaovrchvodybqnymxfjnxwekukimdvieaffedgskvyeavexnzirzkhrzinbztvpfiqkshlklbuvoodhhytmevvelvuiennquhvernefdakmrkmlyqgkalpkvpuebrpjldpgifrwtbgzyzpzphtspkuagwmllbwfqemtoilwmeaxwxmickrgcirimplrrnrzvdntzzxwgniqylgqbdhadpikvlqhwgfzpaasantalivedasadevilatnasaohyvdilgsrweeyvsggzsxchjfiipsyyzdtufunsatjqjfoewwkwpvenchdlwdyfwbyomqoafcrbqdmzswmbblrsodjcxfyrqazafuywvddiooiipmoxjdbnxzbngrakfnzshaocrqcwggehnneaurbaytjymafsbzemuzpwjshwxjvmjnufabdeluajkdvoobnnwmozdpzbdrewgawaluggpcvdjqpvjsyvuidrwarmokuyscbgoppmuojnnrihkmrnmtdfysmcazubukxegqrkapsoxofsaotapqajeoqdnwxewysuhwdlyltzftvefdhvdhxxhqmmozjzoamycjejbyxjakhfiilynvjvrmxndssgdfmnqxaxmnaelcmqpcotsqnhlmobexlrbvjylvfyerdklltrnluxtimgeuacpqefqxwlsbgcsjiwfzpimcsmmyniczsbgyovoldkfcxsfqxzaekyspjzmvkbroffwnhatbwqesan'
    TC4 = 'zgmexkfvxgxroqtqajchdkduyclujuynanabbenvwlgwotyttrgiqdrecawxknglmcjtywpkfssyfmcouvgeonwaoopirarzeumyeuqahljfgvcowmggixozqhwayonrabxxjznqprsdcxutxiorghnfxvkiuhyryflkitgvajoylsomyuzwoyhvzudfxgdbqiwtitgwuwgqdnperrizowlsuwotzvpzroraivbrrrreybmpyzvffeiuugrsgyaqhitxhigkvbnfmdvlllcvthqgqdxuqjtyifteosfxwhbilhunflosaejntksiqxgwcblrwxxrywqlmqgtskpzhkwrendrnqzsnccmanbjmlcvaxcfhzqiyrtmmtitoykoeueudqjcvnoxlspkwlvwvznocdwfhicoryfonjolqnfeuvlfnkqitxqgbkwyrvhkjuhtlvtosrhdjsmdmqhrlmbgkgdgylneymqqlyfkfuvacnziqnvruhhyzfitcsyxdcaolsnatiwvtkvihbbxisfeohhccnlkktjwyfnihsoklbzodcexjlfvfyrukxzyltqjwfleqnzvlvuypvktqixjpritjpbzjrxutdpkkurgelhvwftzzkjdpnlcdtrivbjlfxwzawvfvxrjworpqaoamlhthekfvnsxemdwlpyoovutksqxnkysblldpgncznuonsaugapresbpjpzhdjcazvpvjentysutczphankwftpxpsciunemvsmtfubjgsuvddyaqvdlxbodbzxbpvhyaeedvmgwmpolhgxjoafkumgzczgasefglyuucwdgoghywioiskaunfbjvxruqtmeieuozeucjhkurtanxzjrztrycfhhwdffrcbcccyclbsyrokpjevpvkbckinhklyudurmcxxpzbjlvaqvunkrrmsllolcxtrexyjcnjwsyhgpmrvrfigskqmilzbkqtlgkdeldohskilpfuoozmedjcsobmvtvkucmoyvwwwaiscngteqgblirticrinhqfbdrhibcgighhsobzkxjephjvxpaefngesfalwityqrvowjtxlxhdubnqbhbdpjemagnedsrxbvcavhiueuznccyaqitirhjxhblghpnxqtzkvoduyceiqcwdntosyvmlmybwfzmeirebxyufzanasthbuwqogellbteepgtibengzpqclwjflqesotgnytpcpuzaitsfqxlqnkmjgfwttfolerjflstzevqwyheblmlotlgsmpbfbodufcvbsbdtgzuytpqikostjjbblzolqbnsoiovelowjjmvigpjlxaygimoyiunzrrylulivwtdlcresppgbefzgxosixlsqirebxccvlltcydloonmvyjmojraqiwflyqfncpspqldcrssnbuluvagmrcrjzhgmoiixpyrrlmjaleasxguyqyvkywwlfqhlvovezznwuutyjioimzlzvwokoqsxrkvdyphjhnoechoikpdulxjkqjbauqtgcnwkkhsmaksdhqhhazycgcurcwwbgrltdrqstdldxjroccstsggyqcfqnwtrrobetewenbtlblmpujfvvvbctsftuhcagugzoeurothxpdbwyzsyczfzpqziigwvlhxdjneovvjuhdrqtstfbrghjlrjwxhftbjdxblnxbtlibltefvhevmqebgqwkkkxcecqgqjfllqtpscvxwvnjadasmrebnfnvpbylfezuzrtnezegkcemfdrtdzevcffdpvvkkucewoxupwqtdpggtidttqtbtlswiccvgpumvfnsvlgaayqgaogyfrvucvmhmgfvcogvyrksdtalnmzulcwueaswqcvzetteoxwukpmdobtkaxbpwbiyrgfoptzzqcrbnydavysbcfwdoqsmfdoowbrbrnsxubmfzcdmbdpvtukfyoomagondpwxmtyrwoaoiqqlaphacsvwpteclmkhzzfuuemhuapnkzbfzgagzuthdwuetweherugwnyanhtefcaqriymfleavmvapjzfknkrhlumaazhjykvrwcjcrfyatbmjzcsccxojvxpnrxwulbbsqntmgqeobqzzvebzdakeywqilcsthjopyniyyrrxvgdbcmtookouvalkfvgtsafsxqizzibuhyshuxvgllyzdrynjwwqivhlybtfakxvuguhtookgvmifxllnpohynhtpxjidebnqbwmnbuzfbqcgehpavmxymvbyrhfltosuruqteblhwpvozriviphdzvrizhhbyolwrfnxtshdrhddjusjukaekaxfxzrblujcvuwwbsbbjeznxnsjyhgvjsxmllzyndblvyqoopclpuxykgdqwygllurofhgyxavytnncckotdwiarlkqoeetrmzrnneseligjakhibumcoiyuclpfblqhtmzfgerfxjwhapvybmrgozwyfloiqbfkxfjbhjztkpzqrxdythdrbuqvztknnvnkzodmyhocxckrsbmgwabrzpmxgcpkhbzqzwvnmffhlbbogvvwlwghzqdicmgnupgsaxirgoylqsvendiyqvybmschpeweckytokjcryvcqmlwbmwdgqqhjvkxohlebfkgjzhgpvivtubmgalveizzshsxvuppbirxewrkcorqrsvnwqlctcisjtmozodwkvbknoesisehaneatorwqeoprobceghyyhpvhgshligsjbmkbntwzktmqyikcieluayqgbqnoxftyckkdndiuicxolpifbuxclzawwcgdslwquajatwinwelucgaifljkxjcsmukjnzsqrhqjiuxijkxvsoglekwahejlgkjmguzradyzatnagdqgbjdgwsxbblrrxsijcczijcvdonndukbzkzzqrgaxgjyaygxexddhusyovwnvdpzyethytaymqrkdunxnpgxhouuahjeqwbaqzmqdexohfooqfftkykzvdxndckknxdxedrbxtuykohvrrvhgsdysjvbojsckccdpnlkzywfnckktaesyfalrqjsgnblniegywuzzstoyudvfojsugjucjvcvfkecgbuylibvolyueviefdeifiedbnbvdtfatjpnwyzxzentraghhakkcwbxniekiykcxmxqsdsplfsyoowvvcushyrjxpkxbkdbewvrvrtrzhzscuihrgjdxnpfkyxjmpouogyeqxrrbpajluxqwwqmjvivqwfrvdzedyrhichtbnhbqnbiiskiqkpiphiyuokvniymgzggkpyasvbgfpaetunafidreiitdfxfxdvfxxwiaxuftikwwyefmextjvvxmgfauxwqwpdrkcmvewbxhuhjoepmaqpaozgocsjbbifbhtpjzzihrjnqlkbmdmvhtkyhlgawkobxpzrvupchpwdagdghtiqgzibazfnaonqzaukxgimxnkawxkfowfflymymcvxidjmvkliuuhbhmovijfjbnggvzprehlqqxatewtyvtsgxjbworsutdhjagdusdnedewckfkhjdrlgpycujspgnnavtapexdbzusdvskwnvjsidfsvfpqpzclhnvmqctlrxfdbeeenevgrbytqvahylokhxwpujwwiirolrndfthkwvxqgjnrjyrynkdlpvwoeanxydhrytwpetrngkmbloykuauyzjbtdaacqrprezwkxgkfqtyjafnvlzwlcuvhqydozsgquedlkrazdxqgxjixhsvmdnnkfqhkythlitkpxocckgegeamcfrjxriusxvcezwgrhrkeasginvpeiqgiutmwrffvtkpvsxybshjxovhpvyeqvkwiilgxpmdvlnmtevepytjswzpckpkdhlncebjupfyaghkktcblmnkhxobblcfefxkhfvqmazjsxspmthislhfgsqzmyeaojgivobqbglfuagbxngnifzrqrdtpmixnneqkoisqdrdbtkoitbzrfiyejpnmivrjbzifohojegavamfdqnddksplkvimttjjwawmtzoudyrvkbmimjsrvbxitpzhrwbdwyhuagzsdoouqsgzvnnzvbzzltkytayjflbwhacxuzkensnpairswycpldbmwmmyhwoubpjzioiswuzvxwoobarexjyfoniofpgllzhurrdkyosuekpajxvdgqfffjoajtxrwamvenljxbkojfmrflxhoaepobqxushizgtbbakwpggznomtjsowvbfajpmykspdbrjvczetnezwutnrsfgxydmfkritnwpkdjndlghddwexnveywrhaznondknvieasirrggczsvkfwhavvqumlrwsjxdpxilhwfxpwypsmlzourzkdijriqlagqsxvcexidvqqftskzlmpckluqgksriwkmxywdrqpuyzcvdyvytfkngluxfsfavlqvwfkjgteqrgypcmbrfudsjjxwagdqxnyydpxtksjpqkdmlniomdflhwlpaqupmonhjrkslfnufmcgfwdlqjsbttgbhjzfwufvtsktayhhdbvxunxaavkupytawcuffwkgbzjsoylknbdciospjyscfkgbavcbzvdnngmfztpiubosbkspatnqziqntgtkcfcyzmjtsulklzckznzxoithcwxmndsjkhtridkovqcclfvclpsozfuleprzzvqwknxyetjoixdvpecjttokyqsqrkaefjknmfpfyyurfpiinwspmkheymgqbrfijelwhmtmekdeidhqkcuxlqxgdspkcnjakqdhutujacfiqfjscmvvxhrwthcrfslvidxnvarjqjlozicsdblrtznsrsuhxegjjsrrxxghdgzqwgkaqjtwosxpqbblmzzaspncczcamebcaovbajlrwmmksvwswkdctnmpnolvfnulvfiqknqppzcjomurcnuxiirLONGESTPALINDROMICSUBSEQUENCE'
    testcases = [TC1, TC2, TC3, TC4]
    for i, testcase in enumerate(testcases):
        lps_length, lps_list = longest_palindrom(testcase)
        print(f"TC {i+1} :")
        print(f"  가장 긴 회문 부분 문자열의 길이 : {lps_length}")
        print(f"  가장 긴 회문 부분 문자열의 목록 : {lps_list}")
              

if __name__ == "__main__":
    main()