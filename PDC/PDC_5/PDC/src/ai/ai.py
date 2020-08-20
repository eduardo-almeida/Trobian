from key_mapping import *
from pdcresource import *
from pdcglobal import *
from actor import Actor

class AI(object):
    game = None
    def __init__(self, actor):
        self.actor = actor
        self.hostile = []
        
    def act(self):
        pass

    def seeing_player(self):
        dis = get_dis(self.actor.x, self.actor.y, self.game.player.x, self.game.player.y)
        if dis > 15:
            return False
        
        blocked = False
        fields = line(self.actor.x, self.actor.y, self.game.player.x, self.game.player.y)
        for f in fields:
            x, y = f
            blocked |= self.game.map.map_array[y][x][MT_FLAGS] & F_BLOCKSIGHT
        return not blocked    
    
    def get_player_direction(self):
        return self.actor.locateDirection(self.game.player)
    
    def build_alternate_dirs(self, dir):
        if dir == MOVE_UP: return [MOVE_UP_LEFT, MOVE_UP_RIGHT]
        if dir == MOVE_DOWN: return [MOVE_DOWN_LEFT, MOVE_DOWN_RIGHT]
        if dir == MOVE_LEFT: return [MOVE_UP_LEFT, MOVE_DOWN_LEFT]
        if dir == MOVE_RIGHT:return [MOVE_UP_RIGHT, MOVE_DOWN_RIGHT]
        if dir == MOVE_WAIT:return []
        if dir == MOVE_UP_LEFT:return [MOVE_LEFT, MOVE_UP]
        if dir == MOVE_DOWN_LEFT:return [MOVE_DOWN, MOVE_LEFT]
        if dir == MOVE_UP_RIGHT:return [MOVE_UP, MOVE_RIGHT]
        if dir == MOVE_DOWN_RIGHT:return [MOVE_DOWN, MOVE_RIGHT]
    
    def move_randomly(self):
        list = []
        
        if d(20) < 10:
            self.actor.move(MOVE_WAIT)
        
        for item in MOVES:
            list.append(item)
            
        random.shuffle(list)
        success = False
        while len(list) > 0 and not success:
            dir = list.pop()
            new_pos = get_new_pos(self.actor.pos(), dir)
            act = self.game.get_actor_at(new_pos)
            if act != None:
                if act not in self.hostile:
                    continue
            success = self.actor.move(dir)

