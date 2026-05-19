import yaml
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any

@dataclass
class TapeConfiguration:
    """Her adımda şeridin anlık durumunu kaydetmek için kullanılan veri sınıfı."""
    state: str
    tape: str
    head_position: int

@dataclass
class RunResult:
    """Çalışma bittiğinde dönecek olan zorunlu sonuç formatı."""
    accepted: bool
    reason: str  # "accept", "no_transition", "timeout"
    final_tape: str
    steps: int
    history: List[TapeConfiguration] = field(default_factory=list)

class Tape:
    """Turing makinesinin şeridini ve kafa hareketlerini yöneten sınıf."""
    def __init__(self, initial_string: str, blank_symbol: str):
        self.blank = blank_symbol
        # Python string'leri immutable olduğu için listeye çevirerek tuzaktan kaçıyoruz
        self.content = list(initial_string) if initial_string else [self.blank]
        
    def read(self, position: int) -> str:
        # Kafa sağa doğru genişleyip listeden taşarsa blank sembolü döndür
        if position >= len(self.content):
            return self.blank
        return self.content[position]
        
    def write(self, position: int, symbol: str):
        # Kafa mevcut listenin sağındaysa, arayı blank sembolü ile doldurarak genişlet
        while position >= len(self.content):
            self.content.append(self.blank)
        self.content[position] = symbol
        
    def to_string(self) -> str:
        """Şeridin anlık string halini üretir."""
        return "".join(self.content)

class SingleTapeTM:
    """Deterministic single-tape Turing Makinesi motoru."""
    def __init__(self, config: Dict[str, Any]):
        self.name = config.get("name", "")
        self.states = config.get("states", [])
        self.blank = config.get("blank", "B")
        self.start_state = config.get("start_state", "")
        self.accept_states = set(config.get("accept_states", []))
        self.reject_states = set(config.get("reject_states", []))
        
        # Hızlı erişim için geçiş tablosunu sözlüğe (dict) çeviriyoruz
        # Yapı: {(mevcut_durum, okunan_sembol): (sonraki_durum, yazilacak_sembol, yon)}
        self.transitions = {}
        raw_transitions = config.get("transitions", [])
        
        for t in raw_transitions:
            key = (t["state"], t["read"])
            self.transitions[key] = (t["next"], t["write"], t["move"])

    @classmethod
    def from_yaml(cls, filepath: str):
        """Zorunlu API: YAML dosyasını okuyup makine nesnesini döndürür."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            return cls(config)
        except Exception as e:
            # Hatalı YAML durumunda ValueError fırlatılması şartnamede zorunludur
            raise ValueError(f"YAML Okuma Hatası: {str(e)}")

    def run(self, input_string: str, max_steps: int = 1000, verbose: bool = False) -> RunResult:
        """Zorunlu API: Verilen girdi dizgisiyle makineyi simüle eder."""
        tape = Tape(input_string, self.blank)
        head_pos = 0
        current_state = self.start_state
        steps = 0
        history = []

        while True:
            current_tape_str = tape.to_string()
            
            # 1. Her adımın durumunu geçmişe (history) kaydet (Zorunlu)
            history.append(TapeConfiguration(
                state=current_state,
                tape=current_tape_str,
                head_position=head_pos
            ))

            # verbose=True ise şartnamede istenen formatta ekrana bas
            if verbose:
                current_char = tape.read(head_pos)
                # Kafanın olduğu karakteri köşeli parantez içine alıyoruz
                left_part = current_tape_str[:head_pos]
                right_part = current_tape_str[head_pos + 1:]
                
                # Gelecek hamleyi ekrana basmak için kuralı kontrol et
                key_check = (current_state, current_char)
                move_str = self.transitions[key_check][2] if key_check in self.transitions else "Durdu"
                
                print(f"Adım {steps} | Durum: {current_state} | Şerit: {left_part}[{current_char}]{right_part} | Hareket: {move_str}")

            # 2. Durum Kontrolleri (Şartnameye uygun nedenlerle dönülür)
            if current_state in self.accept_states:
                return RunResult(True, "accept", current_tape_str, steps, history)
                
            if current_state in self.reject_states:
                return RunResult(False, "reject", current_tape_str, steps, history)

            if steps >= max_steps:
                return RunResult(False, "timeout", current_tape_str, steps, history)

            # 3. Geçiş Kuralını Bulma
            current_char = tape.read(head_pos)
            key = (current_state, current_char)
            
            if key not in self.transitions:
                # Geçerli kural yoksa durur
                return RunResult(False, "no_transition", current_tape_str, steps, history)

            # 4. Kuralı Uygulama
            next_state, write_char, move = self.transitions[key]
            tape.write(head_pos, write_char)
            current_state = next_state
            
            # Kafa Hareketi ve Sola Taşma Yönetimi
            if move == "R":
                head_pos += 1
            elif move == "L":
                head_pos -= 1
                # Kafa sola taştığında ne yapacağımızı README'de belirterek 0'da sabitliyoruz
                if head_pos < 0:
                    head_pos = 0

            steps += 1

           