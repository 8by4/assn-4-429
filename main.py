from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
        
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
        
    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")
    if input("Is your budget medium? (y/n): ").lower().startswith("y"):
        facts.append("budget_medium")
    if input("Is your budget low? (y/n): ").lower().startswith("y"):
        facts.append("budget_low")
        
    if input("Is your purpose gaming? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Is your purpose creative work? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Is your purpose office work? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
        
    if input("Is your preferred operating system windows? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_windows")
    if input("Is your preferred operating system mac? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_macos")
    if input("Is your preferred operating system linux? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_linux")
        
    if input("Do you need ai acceleration? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
        
    if input("Do you need a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")\
            
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
        
        
    return facts

def main():
    facts = collect_initial_facts()
    
    engine = ForwardChainingEngine(load_rules(KB_PATH))
    
    engine.assert_facts(facts)
    engine.run()
    
    conclusions = engine.conclusions()
    
    print("\n .......Results.......")
    
    if conclusions["recommendations"]:
        for r in conclusions["recommendations"]:
            rec_name = r.replace("recommend:", "")
            trace_item = next(t for t in conclusions["trace"] if t["added"] == r)
            print(f"> Recommendation: {rec_name}")
            print(f"> Explanation: derived from rule '{trace_item['rule']}'\n")
            
    if conclusions["specs"]:
        print("\n .......Recommended Specs.......")
        for s in conclusions ["specs"]:
            print(".", s.replace ("spec:", ""))
            
            
    print("\n .......Rules Fired.......")
    for t in conclusions ["trace"]:
        print(f"- {t['rule']}  (added: {t['added']})")

if __name__ == "__main__":
    main()
