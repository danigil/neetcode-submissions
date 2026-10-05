import json
class Solution:
    """
    Protocol:
    s = 1234567890 <offset_arr> strs 
    """
    def encode(self, strs: List[str]) -> str:
        lens = [len(s) for s in strs]
        lens_json_str = json.dumps(lens,indent=None,separators=(',', ':'))
        s_len = len(lens_json_str)

        s_len_str = f'{s_len:010}'
        
        ret = f'{s_len_str}{lens_json_str}{''.join(strs)}'
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        n_len=10
        
        s_len_str = s[:n_len]
        s=s[n_len:]

        s_len=int(s_len_str)
        lens_json_str = s[:s_len]
        lens = json.loads(lens_json_str)
        s = s[s_len:]

        offset=0
        ret = []
        for l in lens:
            ret.append(s[offset:offset+l])
            offset+=l

        return ret
