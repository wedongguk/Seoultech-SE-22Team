import pytest
from Data.GAME_LOGIC.uno_PlayerList import PlayerList
from Data.GAME_LOGIC.uno_Player import Player

def test_size():
    p1 = Player("user1", True)
    p2 = Player("user2", False)
    player_list = [p1, p2]
    pl = PlayerList(player_list)
    assert pl.size() == 2

def test_nextTurn():
    p1 = Player("user1", True)
    p2 = Player("user2", False)
    player_list = [p1, p2]
    pl = PlayerList(player_list)
    assert pl.turnIdx == 1
    pl.nextTurn()
    assert pl.turnIdx == 0

def test_skip():
    p1 = Player("user1", True)
    p2 = Player("user2", False)
    p3 = Player("user3", False)
    player_list = [p1, p2, p3]
    pl = PlayerList(player_list)
    pl.nextTurn()
    assert pl.nextIdx == 1
    pl.skip()
    assert pl.nextIdx == 2

def test_reverse():
    
    ## 3명 이상
    p1 = Player("user1", True)
    p2 = Player("user2", False)
    p3 = Player("user3", False)
    player_list = [p1, p2, p3]
    pl = PlayerList(player_list)
    pl.nextTurn()
    assert pl.turnIdx == 0
    assert pl.direction == 1
    pl.reverse()
    pl.nextTurn()
    assert pl.direction == -1
    assert pl.turnIdx == 2
    pl.reverse()
    pl.nextTurn()
    assert pl.direction == 1
    assert pl.turnIdx == 0
    
    ## 2명
    player_list = [p1, p2]
    pl = PlayerList(player_list)
    pl.nextTurn()
    assert pl.turnIdx == 0
    assert pl.direction == 1
    pl.reverse()
    pl.nextTurn()
    assert pl.turnIdx == 0
    assert pl.direction == -1

def test_turnPlayer():
    p1 = Player("user1", True)
    p2 = Player("user2", False)
    p3 = Player("user3", False)
    player_list = [p1, p2, p3]
    pl = PlayerList(player_list)
    assert pl.turnPlayer() == p3
    
    pl.nextTurn()
    assert pl.turnPlayer() == p1

def test_prevPlayer():
    p1 = Player("user1", True)
    p2 = Player("user2", False)
    p3 = Player("user3", False)
    player_list = [p1, p2, p3]
    pl = PlayerList(player_list)
    assert pl.prevPlayer() == p2
    
    pl.nextTurn()
    assert pl.prevPlayer() == p3

def test_nextPlayer():
    p1 = Player("user1", True)
    p2 = Player("user2", False)
    p3 = Player("user3", False)
    player_list = [p1, p2, p3]
    pl = PlayerList(player_list)
    assert pl.nextPlayer() == p1
    
    pl.nextTurn()
    assert pl.nextPlayer() == p2

def test_idxPlayer():
    p1 = Player("user1", True)
    p2 = Player("user2", False)
    player_list = [p1, p2]
    pl = PlayerList(player_list)
    assert pl.idxPlayer(0) == p1

def test_uti():
    p1 = Player("user1", True, 100)
    p2 = Player("user2", False)
    player_list = [p1, p2]
    pl = PlayerList(player_list)
    assert pl.uti(100) == 0

def test_lst():
    p1 = Player("user1", True)
    p2 = Player("user2", False)
    player_list = [p1, p2]
    pl = PlayerList(player_list)
    assert pl.lst() == player_list
        
    
