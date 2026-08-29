class LRUCache {
public:
    LRUCache(int capacity) :capacity_(capacity) {

    }
    
    int get(int key) {
        auto it = mp.find(key);
        if (it == mp.end()) {
            return -1;
        }
        auto cache_it = it->second; 
        pair<int, int> key_val = *cache_it;

        // move node to back of dll, most recent
        dll.splice(dll.end(), dll, cache_it);

        return key_val.second;
    }
    
    void put(int key, int value) {
        auto found = mp.find(key);
        if (found != mp.end()) {
            found->second->second = value;
            dll.splice(dll.end(), dll, found->second);
            return;
        }
        
        if (dll.size() == capacity_) {
            // evict LRU from beginning of dll and map
            auto it = dll.begin();
            int rem_key = it->first;
            dll.erase(it);
            mp.erase(rem_key);
        }
        dll.push_back(pair<int, int>(key, value));
        auto it = prev(dll.end());
        mp[key] = it;
    }

private:
    int capacity_;
    unordered_map<int, list<pair<int, int>>::iterator> mp; // key, node
    list<pair<int, int>> dll; // holds keys, values
};
