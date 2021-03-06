# 帝國火星曆に就て

我々は、我が國(日本帝國)と同君聯合を爲す國家たる火星帝國に於る曆法「帝國火星曆」での日時と地球の曆との換算を實現する爲の程序を製作しました。以下此の文章では、帝國火星曆の理念及び仕組に就て述べ、亦、地球の曆法から帝國火星曆への換算法、及び其の換算程序の作成に用ゐた曆學上の用語に就て解説します。

## 帝國火星曆の理念

火星帝國の文化を語る上で缺かせない要素の一つとして、火星の獨特の曆があります。火星帝國の初期の住民は地球の樣々な文化圈から移住した人々と其の子孫でしたが、文化的・政治的に其の中核を爲したのは我が國からの移住者と其の子孫でした。火星開拓の初期に當る時代、我が國の火星に於る影響力の擴大と反比例する樣に地球圈に於る我が國の威信は低迷の一途を辿ってゐました。此の樣な時代背景から當時の火星移民の中には、衰亡し行く我が國の文化と理念を繼承し発展させる理想的な國家を火星に建設すると云ふ考へが流行してゐました。さう云ふ訣で、火星に移住した人々は、我が國の年中行事を火星のカレンダー上で再現する爲に色々の工夫を凝らしました。斯うして曆に關する我が國の風習と火星の運行とを折衷して誕生したのが、帝國火星曆なのです。

## 紀元に就て

火星の曆で年を數へるに當ってどの年を元年とするべきかに就ては、ガリレオ・ガリレイが最初に望遠鏡で火星を觀測した年、火星觀測に功績のあったカール・ランプランドの生まれた年(後述の Mars Sol Date を參照)、バイキング 1 號が火星に著陸した年、人類が初めて火星に著いた年、火星帝國の首都である高天原市が建設された年、火星帝國が樹立された年など、多數の基準が提案されました。火星帝國が最終的に公式に採用したのは、我が國の曆と同じ基準、卽ち、神武天皇の卽位の年を元年とする物でした。此の方式は、我が國からの火星植民者達によって古くから使はれてをり、亦た我が國の文化を繼承すると云ふ火星帝國の國是を反映する物です。

## 火星の 1 年と置閏法

帝國火星曆の 1 年は(火星帝國の首都高天原市の存在する)火星の北半球に於る冬至から次の冬至の迄の長さを基準に決められてゐます。此の長さを冬至囘歸年と云ひます。冬至の日時は天文學的な觀測と豫測によって定められてゐます。冬至囘歸年の長さは 668.596 火星日です。曆上の 1 年の日數は整數でないと行けないので、帝國火星曆では 668 日から成る平年と 669 日から成る閏年が規則的に巡って來る仕組に成ってゐます。1000 年閒に 596 囘閏年が來ます。閏年の方が平年より多い事に成ります。

閏年の決め方は以下の通りです。先づ年の下一桁が 0･1･3･5･7･9 に成る年を閏年とします。其の內で年が 250 で割り切れる年を平年に戾します。斯うして 1000 年閒に 600 - 4 = 596 囘の閏年を得ます。

尚、閏日は次節に述べる樣に 24 月 27 日の後に置きます。

## 火星の「月」

火星の人々は、1 年を 24 個の「月」に分割する事にしました。一つの月は、日數の多い大の月は 28 日、日數の少ない小の月は 27 日から成り、槪ね地球の 1 箇月と同じ長さです。1〜5 月、7〜11 月、13〜17 月、19〜23 月は大の月。6 月と 12 月と 18 月は小の月。24 月は閏年には大の月、平年には小の月に成ります。

1 月 1 日をどの日にするか決めるに當って、火星の人々は我が國の傳統的な曆の作り方を火星に應用する事にしました。我が國の舊曆では、先づ冬至の日を決め、冬至を基準に 1 年を 24 分割して 24 の「節氣」の日を決め、冬至を 0 番目として 4 番目の節氣を含む月を 1 月とする事で 1 月 1 日が概ね 3 番目の節氣たる立春の前後に來る樣にします。(我が國の舊曆では 1 年を節氣で 24 分割する際〈黃道〉を 24 等分し太陽が各〻の分割點を通過する瞬閒を節氣としてゐます。此の樣に太陽の位置に基づいて節氣を置く手法を定氣法と云ひます。一方火星では、1 年の〈日數〉を 24 等分する事で各月の 1 日が節氣と對應する樣にしました。此の樣に時閒を等分して節氣を置く手法を恆氣法と云ひます。我が國でも現在の舊曆である天保曆が採用される前迄は恆氣法が用ゐられてゐました。)24 箇月ある火星の各月の 1 日が 24 の節氣に對應すると考へると、冬至が 22 月 1 日に來る樣にすれば 3 箇月後の 1 月 1 日に立春が來る事に成ります。斯う云ふ訣で、帝國火星曆では最初に冬至の日を 22 月 1 日と定め、其の 3 箇月後を 1 月 1 日と定める仕組に成ってゐます。(正確には、閏年の關係で冬至の日と 22 月 1 日は少しずれる事があります。)月と節氣を對應させた事から、火星では 1 月を立春月、2 月を雨水月……と云ふ風に、月を節氣の名前で呼ぶ事があります。

## 火星の日・時・分・秒

太陽系には「日」に當る時閒尺度が二つあります。地球日と火星日です。夫々地球と火星の自轉 1 囘に相當する時閒です。火星の 1 日は地球時閒で 24 時閒 39 分 35 秒餘りで地球の 1 日より少々長めですが、生活に支障を來す程の差はありません。此の爲、火星では生活上の 1 日は火星の自轉周期を基に定められてをり、此れを火星日と稱します。月球(一晝夜=約 29.5 地球日)やガニメデ(一晝夜=約 7.2 地球日)など、地球と火星以外の天體では、ヒトの槪日周期(寢て起きて復た寢る迄の周期)と自轉周期の差が大きいので、生活上の 1 日は地球日若しくは火星日によって決められてゐます。火星日は火星の他に、火星帝國と深い繫がりを有する木星圈諸國等で使はれてゐます。

火星で時刻を表すのに使はれる時・分・秒は、火星の 1 日を 24 時閒/1440 分/86400 秒とする爲に各々地球の約 1.0275 倍の長さに成ってゐます。

火星日を使ふ諸國で時刻の基準と成ってゐるのは、火星帝國の首都高天原市を通る子午線(現在の基準では東經 0 度、嘗て使はれてゐた惠在(ゑあり)子午線基準では西經 135 度)に依って定められてゐる高天原標準時です。高天原市から見て平均太陽(黃道上を太陽の平均速度と同じ速度で移動する假想的な天體)が天底に來る時刻が高天原標準時での 0 時 0 分に相當します。火星には高天原標準時の他に各地の子午線による地方時間も幾つか存在してゐます。

## 地球の曆との共通點と相違點

### グレゴリオ曆との共通點

- 惑星の公轉 1 囘を 1 年とする太陽曆である。
- 惑星の自轉 1 囘を 1 日とする。
- 月の日數は固定されてゐる。
- 曆のずれは閏日を置いて解決する。

### グレゴリオ曆との相違點

- 帝國火星曆は火星の公轉を 1 年とするが、グレゴリオ曆は地球の公轉を 1 年とする。
- 帝國火星曆は火星の自轉を 1 日とするが、グレゴリオ曆は地球の自轉を 1 日とする。
- 帝國火星曆の 1 年は 24 箇月から成るが、グレゴリオ曆の 1 年は 12 箇月から成る。
- 帝國火星曆の 1 月は 27-28 日から成るが、グレゴリオ曆の 1 月は 28-31 日から成る。
- 帝國火星曆は冬至を基準として 1 年の始まりを決めるが、グレゴリオ曆は春分を基準として 1 年の始まりを決める。
- 帝國火星曆は初代天皇たる神武天皇の卽位を元年として數へるが、グレゴリオ曆は基督敎に於て救世主とされるイエスの生誕を元年として數へる。

### 我が國の舊曆との共通點

- 惑星の自轉 1 囘を 1 日とする。
- 冬至を基準として 1 年の始まりを決める。
- 神武天皇の卽位を元年として數へる。

### 我が國の舊曆との相違點

- 帝國火星曆は太陽曆であるが、我が國の舊曆は太陰太陽曆である。
- 帝國火星曆は火星の公轉を 1 年とするが、我が國の舊曆は 12-13 朔望月を 1 年とする。
- 帝國火星曆は 27-28 日を 1 月とするが、我が國の舊曆は 1 朔望月を 1 月とする。
- 帝國火星曆は火星の自轉を 1 日とするが、我が國の舊曆は地球の自轉を 1 日とする。
- 帝國火星曆は曆のずれを閏日を置く事で解決するが、我が國の舊曆は閏月を置く事で解決する。

## 地球の曆と帝國火星曆との換算法

地球の曆から帝國火星曆への換算は、大凡以下の樣な流れで行はれます。

- 地球の曆の日時(世界時)に對應するユリウス通日と ΔT(デルタ・ティー)とを求め、此れを合算して地球時に對應するユリウス通日を求める。
- 地球時に對應するユリウス通日から帝國火星日を求める。
- 帝國火星日から對應する帝國火星曆の日時を求める。

### 世界時、地球時、そして ΔT

先づ「世界時」と「地球時」に就て述べます。世界時(UT: Universal Time)と云ふのは、地球の自轉に基づく時刻の仕組です。何種類かある世界時の一つ、UT1 は、東經 0°(ロンドンのグリニッヂ天文臺を通る子午線)に於る平均的な太陽の動きを恆星の子午線通過等の觀測から求め、其處から地球の自轉軸のぶれによる影響を除去する事で得られる地球の眞の囘轉角により決定される時刻です。UT1 は地球の自轉に最も忠實な時刻ですが、地球の自轉速度は一定ではなく、亦、秒の定義自體が地球の自轉の 86400(= 24 × 60 × 60)分の 1 から僅かにずれた長さに設定された歷史的經緯により、原子時計の進み方で定義される物理的に正確な時刻とは少しづつずれて行きます。

一方で地球時(TT: Terrestrial Time)と云ふのは、地球の自轉とは無關係に原子時計の進み方のみによって定義される時刻の仕組です。地球の自轉の不安定さに影響されない爲、天文學的な現象の觀測や豫測に利用されてゐます。地球時は、地球上の多數の原子時計の觀測によって定義される時刻である國際原子時(TAI: Temps Atomique International)から正確に 32.184 秒進んだ時刻として表されます。此のずれは歷史的理由による物です。

私達が普段使ってゐる時刻は、世界時の一種である協定世界時(UTC: Universal Time, Coordinated)を基に決定されてゐます。協定世界時は謂はば先述の UT1 と TAI の折衷による時刻で、UT1 とのずれは恆に 0.9 秒以內に成る樣に、且つ、TAI とのずれは恆に整數秒に成る樣に調整されてゐます。(「閏秒」とは此の調整の爲に數年に 1 度 UTC を 1 秒晚らせる物です。)

さて、地球の日時から火星の日時を算出するには世界時を基に地球時を算出する必要があります。世界時の UT1 と地球時(TT)との差を ΔT(デルタ・ティー)と云ひ、TT - UT1 = ΔT として定義されます。ΔT の値は、皇紀 2630 年(基督紀元 1970 年)頃から現在に就ては天文觀測により正確に求められてゐます。亦、紀元前 1340 年(基督紀元前 2000 年)頃から現代迄の ΔT は當時の日蝕や月蝕の觀測記錄を基に、現代から 1000 年後程度の未來の ΔT は地球運動のシミュレーションを基に推算されてゐます。

### ユリウス通日と帝國火星日

曆の上で表現される日時は何年何月何日何時何分何秒と云った形に成ってをり、二つの時點の閒の經過時閒を算出するのは面倒です。計算を簡單にする爲、天文學や曆學では「ユリウス通日」を使ひます。ユリウス通日とは、ユリウス曆紀元前 4713 年(皇紀紀元前 4053 年)1 月 1 日 12 時(但し協定世界時基準)からの經過日數です。日より下の單位は小數として扱ひます。グレゴリオ曆の日時をユリウス通日に換算する函數は古くから知られた物があり簡單に計算出來ます。斯うして得た世界時のユリウス通日に、先述した ΔT を加味する事で、地球時のユリウス通日表示を得る事が出來ます。先述した樣に、樣々な天文現象の觀測や豫測は此の地球時を基に行ひます。火星の日時の計算も同樣です。

ユリウス通日の火星版に當る物が帝國火星日であり、此れは帝國火星曆紀元前 1 年 1 月 1 日 0 時(高天原標準時)からの經過日數です。帝國火星日(ISN: Imperial Sol Number)と地球時のユリウス通日表示(JDTT)は、以下の樣な關係を有します。

ISN = (JDTT - 2451549.5) / 1.0274912517 + 945990.6240374

帝國火星日が求まれば、後は紀元からの經過日數によって日附と時刻を順に計算して行く事が出來ます。

## 此のプログラムに就て

此のプログラムは、地球で廣く使はれてゐるグレゴリオ曆と帝國火星曆との變換、其れらの變換中に經由する各種の曆法との變換、火星の季節を表現する上で良く用ゐられる火星中心太陽黃經の算出を目的とする物です。以下に各種の曆法/用語に就て解説します。

### Gregorian Date Time: グレゴリオ曆での日附と時刻

グレゴリオ曆は基督敎圈諸國を始めとする國々で使はれてゐる曆法で、我が國や中華帝國などでも倂用せられてゐます。地球の公轉周期・自轉周期を基準とする太陽曆の一つです。時のローマ教皇グレゴリウス 13 世の命により、其れ以前に使用されてゐたユリウス曆のずれを解消する爲、皇紀 2242 年(基督紀元 1582 年)に制定されました。

### Julian Day: ユリウス通日

ユリウス曆紀元前 4713 年 1 月 1 日 12 時(但し協定世界時(グリニッヂ標準時)基準)から何日經ったかを數へ上げた日數です。天文學で天體の運動の計算等に用ゐられます。

### Terrestrial Time: 地球時

(世界時による)ユリウス通日は地球の自轉を基準に日を加算して行きますが、實際には地球の自轉速度は一樣ではなく不規則に變動してゐますので、未來或いは過去に向ふ程に正確且つ一定な時閒の流れとの閒にずれを生じます。地球の自轉によって定まる世界時(UT: Universal Time)に對して、地球の自轉の影響を受けずに一定速度で進む時閒を地球時(TT: Terrestrial Time)と稱します。世界時と地球時の閒のずれを、ΔT と稱します。過去の ΔT の大きさは、古代人が觀測した日蝕や月蝕の記錄を基に推算されてゐます。

### Mars Ls(Areocentric Solar Longitude): 火星中心太陽黃經

火星での季節を知る目安と成る數値として、火星中心太陽黃經(Ls)があります。此れは、火星から見た太陽の黃道上の經度です。Ls=0° の時に太陽は春分點上にあり、Ls=90° の時は夏至點、Ls=180° の時は秋分點、Ls=270° の時は冬至點にあります。Ls=0° から 90° の閒が天文學上は北半球の春、南半球の秋に當り、以下順繰りに季節が巡ります。

### Mars Sol Date & Imperial Sol Number: マーズソルデートと帝國火星日

火星に於て地球のユリウス通日の樣に基準日からの經過日數を數へる方法として、マーズソルデートと帝國火星日があります。マーズソルデートは、米國の天文學者によって提案されたもので、グリニッヂ標準時の正午と惠在標準時の正子が一致し、且つ地球と火星の夫々から見た黃道上の太陽の經度が一致する日である皇紀 2533 年(基督紀元 1873)年 12 月 29 日から數へ始める方式です。(此の日は偶然にも、米國の天文學者カール・オットー・ランプランドの生誕日です。彼はローウェル天文臺で天體寫眞撮影裝置を設計し、火星の運河の寫眞を撮影したり、赤外線による惑星の溫度觀測を行ふ等の業績を殘しました。)一方、帝國火星日は帝國火星曆 0 年(紀元前 1 年)1 月 1 日の高天原標準時 0 時から數へ始める方式です。帝國火星日はマーズソルデートと 901194.625 火星日ずれてゐます。

### Imperial Date Time: 帝國火星曆での日附と時刻

上述の帝國火星曆での日附と時刻です。

# 帝國火星曆計算プログラムに就てのメタい話。

此のプログラム及び文章は、橘榛名らによるシェアードワールド「兩河世界」の内部に於て火星帝國により再建された日本帝國の住人が火星帝國の曆に就てプログラムと解説を製作した、と云ふ體で製作された物です。文章中にある地名「惠在(ゑあり)」は、實際の火星に於て本初子午線を定義してゐる Airy(エアリー)クレーターに相當してゐます。亦、火星帝國の首都「高天原(たかまのはら、若しくは、たかまがはら)」は、火星の最高峰オリンポス山の近邊にあり、Airy クレーターを基準とする經度で西經 135 度線上にあります。

火星に就ての創作をしてをり獨自の火星曆を運用したい方、又は天文學/曆學上の興味から此のプログラムを見付けた方の爲に解説して置くと、此のプログラムと文章內で用ゐた「帝國火星曆」と「帝國火星日」以外の曆法上の槪念・用語は實在の物と同義であり、其れ等の計算式は NASA(アメリカ航空宇宙局)などがインターネット上に公開した物を引用してゐます。(但し、ΔT 計算式の一部に、皇紀 2679 年(基督紀元 2019 年)迄の現實世界の閏日插入に追隨する樣に獨自の修正を施した部分があります。)其の爲、此のプログラムが提供する Mars Sol Date と Mars Ls の數値を用ゐる事で、あなたは自分丈のオリジナルの火星曆を創る事も可能です。Mars Ls は火星の季節の狀態を表す數値、Mars Sol Date は火星の自轉の狀態を表す數値に當ります。詳細は上記解説文と參考文獻を御覽下さい。

## 參考ページ

NASA — Polynomial Expressions for Delta T

[https://eclipse.gsfc.nasa.gov/SEhelp/deltatpoly2004.html](https://eclipse.gsfc.nasa.gov/SEhelp/deltatpoly2004.html)

NASA GISS: Mars24 Sunclock — Algorithm and Worked Examples

[https://www.giss.nasa.gov/tools/mars24/help/algorithm.html](https://www.giss.nasa.gov/tools/mars24/help/algorithm.html)

A post-Pathfinder evaluation of areocentric solar coordinates with improved timing recipes for Mars seasonal/diurnal climate studies

[https://pubs.giss.nasa.gov/docs/2000/2000_Allison_al05000n.pdf](https://pubs.giss.nasa.gov/docs/2000/2000_Allison_al05000n.pdf)

Astro Commons

[http://astronomy.webcrow.jp/index.html](http://astronomy.webcrow.jp/index.html)
