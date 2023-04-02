def canUse(TopCard_N, TopCard_C, TopCard_CC, TopCard_CN ,ChkCard_N, ChkCard_C): # 카드를 낼 수 있는지 체크하는 메서드

        if (TopCard_N == ChkCard_N) and (TopCard_N > -1): # 숫자 같으면 낼 수 있음
            return True
        
        if (TopCard_C == ChkCard_C) and (TopCard_C > -1): # 색깔 같아도 낼 수 있음
            return True
        
        if (TopCard_C == -1) and (TopCard_CC == ChkCard_C): # 바뀐 색이 같아도 낼 수 있음.
            return 
        
        if (TopCard_N == -1) and (TopCard_CN == ChkCard_N): # 바뀐 숫자가 같아도 낼 수 있음.
            return True
        
        if (ChkCard_C == -1): # 색이 없는 카드는 언제든 낼 수 있음.
            return True

        return False # 이상의 조건을 통과하지 못했다면 내지 못함.

