---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by wangxiaofeng.
--- DateTime: 2020/10/16 7:50 PM
---

function move(nPos, szSrc, szDist)
    --print("Move " .. nPos .. " from " .. szSrc .. " to " .. szDist)
    print(string.format("Move %d from %s to %s", nPos, szSrc, szDist))
end

function hanoi(nCnt, x, y, z)
    if 1 == nCnt then
        move(nCnt, x, z)
    else
        hanoi(nCnt - 1, x, z, y)
        move(nCnt, x, z)
        hanoi(nCnt - 1, y, x, z)
    end
end

hanoi(3, "x", "y", "z")