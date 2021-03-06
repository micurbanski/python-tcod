#!/usr/bin/env python3
# To the extent possible under law, the libtcod maintainers have waived all
# copyright and related or neighboring rights for this example.  This work is
# published from: United States.
# https://creativecommons.org/publicdomain/zero/1.0/
"""An demonstration of event handling using the tcod.event module.
"""
import tcod
import tcod.event


def main():
    """Example program for tcod.event"""
    WIDTH, HEIGHT = 120, 40
    TITLE = None

    with tcod.console_init_root(
        WIDTH,
        HEIGHT,
        TITLE,
        order="F",
        renderer=tcod.RENDERER_SDL2,
        vsync=True,
    ) as console:
        while True:
            tcod.console_flush()
            for event in tcod.event.wait():
                print(repr(event))
                if event.type == "QUIT":
                    raise SystemExit()
                elif event.type == "MOUSEMOTION":
                    console.ch[:, -1] = 0
                    console.print(0, HEIGHT - 1, str(event))
                else:
                    console.blit(console, 0, 0, 0, 1, WIDTH, HEIGHT - 2)
                    console.ch[:, -3] = 0
                    console.print(0, HEIGHT - 3, str(event))


if __name__ == "__main__":
    main()
