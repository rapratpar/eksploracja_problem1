------------------------------ First method: ----------------------------------
Baseline Alignment:

Oblicz średnią globalną wszystkich ocen.

Dla każdego użytkownika oblicz jego bias (o ile średnio odbiega od średniej globalnej).

Dla każdego filmu oblicz jego bias.

Twoja funkcja rate powinna zwracać: score=mean+bias_user+bias_movie.

----------------------------  Second method: -------------------------------
Wide & Deep Learning
Wide + Deep: Model składa się z dwóch części działających równolegle: szerokiej (Wide) i głębokiej (Deep). Wynik końcowy to suma ich "opinii".

Część WIDE (Zapamiętywanie): Działa jak prosta regresja. Uczy się konkretnych reguł na pamięć, np. "Użytkownik X zawsze daje 5 gwiazdek filmom z serii Star Wars". Jest świetna do wyłapywania oczywistych schematów.

Część DEEP (Generalizacja): To wielowarstwowa sieć neuronowa z embeddingami. Szuka ukrytych powiązań. Nawet jeśli nigdy nie oglądałeś niszowego anime, sieć Deep zauważy, że lubisz dynamiczny montaż i mroczny klimat, więc może Ci je zaproponować.
W skrócie: Wide & Deep to próba połączenia logiki ("pamiętam, co lubisz") z intuicją ("czuję, że to też Ci podejcie").

---------------------------  Third method: -------------------------------
SVD++ to ulepszona wersja klasycznego algorytmu SVD (Singular Value Decomposition)

Fundament (Klasyczne SVD): Algorytm rozbija macierz ocen na dwie mniejsze: jedną opisującą użytkowników i drugą opisującą filmy. Każdy film i użytkownik dostaje zestaw ukrytych cech (np. "akcja", "budżet", "klimat").

Problem "Milczącej Większości": Klasyczne SVD bierze pod uwagę tylko wystawione oceny (gwiazdki). Ignoruje fakt, że sam wybór filmu do obejrzenia też coś o nas mówi.

Magia "++" (Implicit Feedback): SVD++ dodaje do wzoru informację o tym, co użytkownik w ogóle obejrzał, nawet jeśli nie wystawił temu oceny (tzw. informacja niejawna).

Przykład: Jeśli obejrzałeś 5 horrorów, ale żadnego nie oceniłeś, SVD++ i tak to uwzględni i uzna, że Twoje preferencje skręcają w stronę strachu.

Modelowanie Profilu: W SVD++ profil użytkownika nie jest stały. Jest on sumą jego "bazowego gustu" oraz wpływu wszystkich filmów, z którymi wszedł w interakcję. Dzięki temu model jest znacznie bardziej precyzyjny.

Killer Funkcja na Konkursy: SVD++ wygrał wiele konkursów (w tym słynny Netflix Prize), ponieważ świetnie radzi sobie z użytkownikami, którzy wystawili mało ocen, ale obejrzeli dużo tytułów.

W skrócie: SVD++ to klasyczne SVD na sterydach, które mówi: "Nie patrzę tylko na to, ile gwiazdek dałeś, ale też na to, co w ogóle zdecydowałeś się włączyć".

--------------------------- Forth method: ------------------------------
NCF (Neural Collaborative Filtering) to model, który mówi: „Skoro mamy sieci neuronowe, to przestańmy ograniczać się do prostego mnożenia macierzy (jak w SVD) i pozwólmy sztucznej inteligencji samej nauczyć się reguł rządzących gustem”.

Zastąpienie matematyki siecią (MLP): W klasycznych systemach (SVD) używa się iloczynu skalarnego (mnożenia liczb). NCF zastępuje to mnożenie wielowarstwową siecią neuronową (Multi-Layer Perceptron), która potrafi wykryć nieliniowe, skomplikowane zależności, których prosta matematyka nie widzi.

Embeddingi jako "DNA" gustu: Użytkownik i film są zamieniani na wektory liczb (embeddingi). Sieć neuronowa dostaje te dwa wektory na wejściu i uczy się, jak je ze sobą "zmiksować", żeby wynik był jak najbliższy prawdziwej ocenie.

Elastyczność: NCF nie zakłada z góry, jak cechy filmu wpływają na ocenę. Sieć może np. odkryć, że dla jednego użytkownika kluczowy jest aktor, a dla innego tylko reżyser, i dostosować do tego swoje przewidywania.

Architektura "Two-Tower": Wyobraź sobie dwie wieże – jedna analizuje użytkownika, druga film. Na samej górze obie wieże łączą się w jedną sieć, która wystawia ostateczny werdykt (ocenę).

Nowoczesny standard: To obecnie fundament większości systemów rekomendacyjnych w dużych serwisach (YouTube, Spotify). Jest bardziej "elastyczny" niż SVD, ale wymaga znacznie więcej danych i czasu na naukę (trening).

W skrócie: NCF to podejście, w którym wyrzucasz sztywne wzory matematyczne do kosza, a w ich miejsce wstawiasz głęboką sieć neuronową, która sama "rozgryza", dlaczego dany użytkownik lubi dany film.
