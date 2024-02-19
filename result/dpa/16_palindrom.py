def longest_palindrom(text):
   n = len(text)
   if n == 0:
       return 0, ""

   isps = [[False] * n for _ in range(n)]
   lp_length = 1

   for i in range(n):
       isps[i][i] = True

   for i in range(n - 1):
       if text[i] == text[i + 1]:
           isps[i][i + 1] = True
           lp_length = 2

   for length in range(3, n + 1):
       for i in range(n - length + 1):
           j = i + length - 1
           if text[i] == text[j] and isps[i + 1][j - 1]:
               isps[i][j] = True
               lp_length = length

   if lp_length == 1:
       return lp_length, []

   lp_list = []
   for i in range(n - lp_length + 1):
       j = i + lp_length - 1
       if isps[i][j]:
           lp_list.append(text[i:j + 1])

   return lp_length, lp_list

def main():
    testcases = [
        'fhdjskbfamanaplanacanalpanamahmfmhkl',
        'oavhdjksqw',
        'wasitacaroracatisaw',
        'zveabcdcbacbetrmhhktbslwnzbdwuopihqhhqxmybqgemlscsyzcsxzztacocatpsxzaljbtanshudeogbsdnujkwqwvclojhxbyilwxbyocnguie',
        'cdbbciconpbxbctvdvcjudwytytqleimpemczcawocxuyepgnmkjuhmmpmvlqbwzmwfblrlurwxrjfcdxaktkilnrwxmnfdxpwvwihwkrmbzykxdyrvlqwyffelkdkinhiymzclpxjhafeticmhrfpvbyaxsecytqxnwqhhhvqgnvwtsgskemgkscdurgfjivivkqdhjnnlbyswmzirzxxfgxvbqlxtgjrsiwofovibpxisafyyiwqqlxyiyjqzdbodrfhizaudszsqtpghajaovrchvodybqnymxfjnxwekukimdvieaffedgskvyeavexnzirzkhrzinbztvpfiqkshlklbuvoodhhytmevvelvuiennquhvernefdakmrkmlyqgkalpkvpuebrpjldpgifrwtbgzyzpzphtspkuagwmllbwfqemtoilwmeaxwxmickrgcirimplrrnrzvdntzzxwgniqylgqbdhadpikvlqhwgfzpaasantalivedasadevilatnasaohyvdilgsrweeyvsggzsxchjfiipsyyzdtufunsatjqjfoewwkwpvenchdlwdyfwbyomqoafcrbqdmzswmbblrsodjcxfyrqazafuywvddiooiipmoxjdbnxzbngrakfnzshaocrqcwggehnneaurbaytjymafsbzemuzpwjshwxjvmjnufabdeluajkdvoobnnwmozdpzbdrewgawaluggpcvdjqpvjsyvuidrwarmokuyscbgoppmuojnnrihkmrnmtdfysmcazubukxegqrkapsoxofsaotapqajeoqdnwxewysuhwdlyltzftvefdhvdhxxhqmmozjzoamycjejbyxjakhfiilynvjvrmxndssgdfmnqxaxmnaelcmqpcotsqnhlmobexlrbvjylvfyerdklltrnluxtimgeuacpqefqxwlsbgcsjiwfzpimcsmmyniczsbgyovoldkfcxsfqxzaekyspjzmvkbroffwnhatbwqesan',
        'zgmexkfvxgxroqtqajchdkduyclujuynanabbenvwlgwotyttrgiqdrecawxknglmcjtywpkfssyfmcouvgeonwaoopirarzeumyeuqahljfgvcowmggixozqhwayonrabxxjznqprsdcxutxiorghnfxvkiuhyryflkitgvajoylsomyuzwoyhvzudfxgdbqiwtitgwuwgqdnperrizowlsuwotzvpzroraivbrrrreybmpyzvffeiuugrsgyaqhitxhigkvbnfmdvlllcvthqgqdxuqjtyifteosfxwhbilhunflosaejntksiqxgwcblrwxxrywqlmqgtskpzhkwrendrnqzsnccmanbjmlcvaxcfhzqiyrtmmtitoykoeueudqjcvnoxlspkwlvwvznocdwfhicoryfonjolqnfeuvlfnkqitxqgbkwyrvhkjuhtlvtosrhdjsmdmqhrlmbgkgdgylneymqqlyfkfuvacnziqnvruhhyzfitcsyxdcaolsnatiwvtkvihbbxisfeohhccnlkktjwyfnihsoklbzodcexjlfvfyrukxzyltqjwfleqnzvlvuypvktqixjpritjpbzjrxutdpkkurgelhvwftzzkjdpnlcdtrivbjlfxwzawvfvxrjworpqaoamlhthekfvnsxemdwlpyoovutksqxnkysblldpgncznuonsaugapresbpjpzhdjcazvpvjentysutczphankwftpxpsciunemvsmtfubjgsuvddyaqvdlxbodbzxbpvhyaeedvmgwmpolhgxjoafkumgzczgasefglyuucwdgoghywioiskaunfbjvxruqtmeieuozeucjhkurtanxzjrztrycfhhwdffrcbcccyclbsyrokpjevpvkbckinhklyudurmcxxpzbjlvaqvunkrrmsllolcxtrexyjcnjwsyhgpmrvrfigskqmilzbkqtlgkdeldohskilpfuoozmedjcsobmvtvkucmoyvwwwaiscngteqgblirticrinhqfbdrhibcgighhsobzkxjephjvxpaefngesfalwityqrvowjtxlxhdubnqbhbdpjemagnedsrxbvcavhiueuznccyaqitirhjxhblghpnxqtzkvoduyceiqcwdntosyvmlmybwfzmeirebxyufzanasthbuwqogellbteepgtibengzpqclwjflqesotgnytpcpuzaitsfqxlqnkmjgfwttfolerjflstzevqwyheblmlotlgsmpbfbodufcvbsbdtgzuytpqikostjjbblzolqbnsoiovelowjjmvigpjlxaygimoyiunzrrylulivwtdlcresppgbefzgxosixlsqirebxccvlltcydloonmvyjmojraqiwflyqfncpspqldcrssnbuluvagmrcrjzhgmoiixpyrrlmjaleasxguyqyvkywwlfqhlvovezznwuutyjioimzlzvwokoqsxrkvdyphjhnoechoikpdulxjkqjbauqtgcnwkkhsmaksdhqhhazycgcurcwwbgrltdrqstdldxjroccstsggyqcfqnwtrrobetewenbtlblmpujfvvvbctsftuhcagugzoeurothxpdbwyzsyczfzpqziigwvlhxdjneovvjuhdrqtstfbrghjlrjwxhftbjdxblnxbtlibltefvhevmqebgqwkkkxcecqgqjfllqtpscvxwvnjadasmrebnfnvpbylfezuzrtnezegkcemfdrtdzevcffdpvvkkucewoxupwqtdpggtidttqtbtlswiccvgpumvfnsvlgaayqgaogyfrvucvmhmgfvcogvyrksdtalnmzulcwueaswqcvzetteoxwukpmdobtkaxbpwbiyrgfoptzzqcrbnydavysbcfwdoqsmfdoowbrbrnsxubmfzcdmbdpvtukfyoomagondpwxmtyrwoaoiqqlaphacsvwpteclmkhzzfuuemhuapnkzbfzgagzuthdwuetweherugwnyanhtefcaqriymfleavmvapjzfknkrhlumaazhjykvrwcjcrfyatbmjzcsccxojvxpnrxwulbbsqntmgqeobqzzvebzdakeywqilcsthjopyniyyrrxvgdbcmtookouvalkfvgtsafsxqizzibuhyshuxvgllyzdrynjwwqivhlybtfakxvuguhtookgvmifxllnpohynhtpxjidebnqbwmnbuzfbqcgehpavmxymvbyrhfltosuruqteblhwpvozriviphdzvrizhhbyolwrfnxtshdrhddjusjukaekaxfxzrblujcvuwwbsbbjeznxnsjyhgvjsxmllzyndblvyqoopclpuxykgdqwygllurofhgyxavytnncckotdwiarlkqoeetrmzrnneseligjakhibumcoiyuclpfblqhtmzfgerfxjwhapvybmrgozwyfloiqbfkxfjbhjztkpzqrxdythdrbuqvztknnvnkzodmyhocxckrsbmgwabrzpmxgcpkhbzqzwvnmffhlbbogvvwlwghzqdicmgnupgsaxirgoylqsvendiyqvybmschpeweckytokjcryvcqmlwbmwdgqqhjvkxohlebfkgjzhgpvivtubmgalveizzshsxvuppbirxewrkcorqrsvnwqlctcisjtmozodwkvbknoesisehaneatorwqeoprobceghyyhpvhgshligsjbmkbntwzktmqyikcieluayqgbqnoxftyckkdndiuicxolpifbuxclzawwcgdslwquajatwinwelucgaifljkxjcsmukjnzsqrhqjiuxijkxvsoglekwahejlgkjmguzradyzatnagdqgbjdgwsxbblrrxsijcczijcvdonndukbzkzzqrgaxgjyaygxexddhusyovwnvdpzyethytaymqrkdunxnpgxhouuahjeqwbaqzmqdexohfooqfftkykzvdxndckknxdxedrbxtuykohvrrvhgsdysjvbojsckccdpnlkzywfnckktaesyfalrqjsgnblniegywuzzstoyudvfojsugjucjvcvfkecgbuylibvolyueviefdeifiedbnbvdtfatjpnwyzxzentraghhakkcwbxniekiykcxmxqsdsplfsyoowvvcushyrjxpkxbkdbewvrvrtrzhzscuihrgjdxnpfkyxjmpouogyeqxrrbpajluxqwwqmjvivqwfrvdzedyrhichtbnhbqnbiiskiqkpiphiyuokvniymgzggkpyasvbgfpaetunafidreiitdfxfxdvfxxwiaxuftikwwyefmextjvvxmgfauxwqwpdrkcmvewbxhuhjoepmaqpaozgocsjbbifbhtpjzzihrjnqlkbmdmvhtkyhlgawkobxpzrvupchpwdagdghtiqgzibazfnaonqzaukxgimxnkawxkfowfflymymcvxidjmvkliuuhbhmovijfjbnggvzprehlqqxatewtyvtsgxjbworsutdhjagdusdnedewckfkhjdrlgpycujspgnnavtapexdbzusdvskwnvjsidfsvfpqpzclhnvmqctlrxfdbeeenevgrbytqvahylokhxwpujwwiirolrndfthkwvxqgjnrjyrynkdlpvwoeanxydhrytwpetrngkmbloykuauyzjbtdaacqrprezwkxgkfqtyjafnvlzwlcuvhqydozsgquedlkrazdxqgxjixhsvmdnnkfqhkythlitkpxocckgegeamcfrjxriusxvcezwgrhrkeasginvpeiqgiutmwrffvtkpvsxybshjxovhpvyeqvkwiilgxpmdvlnmtevepytjswzpckpkdhlncebjupfyaghkktcblmnkhxobblcfefxkhfvqmazjsxspmthislhfgsqzmyeaojgivobqbglfuagbxngnifzrqrdtpmixnneqkoisqdrdbtkoitbzrfiyejpnmivrjbzifohojegavamfdqnddksplkvimttjjwawmtzoudyrvkbmimjsrvbxitpzhrwbdwyhuagzsdoouqsgzvnnzvbzzltkytayjflbwhacxuzkensnpairswycpldbmwmmyhwoubpjzioiswuzvxwoobarexjyfoniofpgllzhurrdkyosuekpajxvdgqfffjoajtxrwamvenljxbkojfmrflxhoaepobqxushizgtbbakwpggznomtjsowvbfajpmykspdbrjvczetnezwutnrsfgxydmfkritnwpkdjndlghddwexnveywrhaznondknvieasirrggczsvkfwhavvqumlrwsjxdpxilhwfxpwypsmlzourzkdijriqlagqsxvcexidvqqftskzlmpckluqgksriwkmxywdrqpuyzcvdyvytfkngluxfsfavlqvwfkjgteqrgypcmbrfudsjjxwagdqxnyydpxtksjpqkdmlniomdflhwlpaqupmonhjrkslfnufmcgfwdlqjsbttgbhjzfwufvtsktayhhdbvxunxaavkupytawcuffwkgbzjsoylknbdciospjyscfkgbavcbzvdnngmfztpiubosbkspatnqziqntgtkcfcyzmjtsulklzckznzxoithcwxmndsjkhtridkovqcclfvclpsozfuleprzzvqwknxyetjoixdvpecjttokyqsqrkaefjknmfpfyyurfpiinwspmkheymgqbrfijelwhmtmekdeidhqkcuxlqxgdspkcnjakqdhutujacfiqfjscmvvxhrwthcrfslvidxnvarjqjlozicsdblrtznsrsuhxegjjsrrxxghdgzqwgkaqjtwosxpqbblmzzaspncczcamebcaovbajlrwmmksvwswkdctnmpnolvfnulvfiqknqppzcjomurcnuxiirLONGESTPALINDROMICSUBSEQUENCE'
    ]
    for i, testcase in enumerate(testcases):
        lps_length, lps_list = longest_palindrom(testcase)
        print(f"Testcase {i+1} :")
        print(f"    가장 긴 회문 부분 문자열의 길이 : {lps_length}")
        print(f"    가장 긴 회문 부분 문자열의 목록 : {lps_list}")
        print()
              

if __name__ == "__main__":
    main()