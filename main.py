def on_life_zero():
    game.over(False, effects.melt)
    music.wawawawaa.play()
info.on_life_zero(on_life_zero)

game.show_long_text("welcome", DialogLayout.BOTTOM)
info.set_life(3)
scene.set_background_color(7)
mySprite = sprites.create(assets.image("""
    player
"""), SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)