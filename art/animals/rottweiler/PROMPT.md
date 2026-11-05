# 罗威纳设计提示词

使用内置 `image_gen`，以 `../labrador/atlas.png` 为编辑参考，启用透明背景。最终采用第一次生成的原图。

Use case: precise-object-edit. Asset type: transparent animation sprite atlas for Umeko Desktop Pets.
Reference/edit target: the Labrador atlas. Replace ALL 24 Labrador dogs with the SAME one beautiful adult ROTTWEILER, retaining the reference's premium soft 2D storybook game-art style, restrained warm dark linework, gentle cel shading, full-animal view, animation concepts and precise FOUR COLUMN by SIX ROW layout. This is a new breed in the same collection.
Canvas EXACTLY 1024 by 1536 pixels; 24 equal 256x256 cells, invisible grid, NO labels, text, panel lines, paper, floor, cast shadows, halo, haze, scenery or props. Genuine transparent alpha=0 empty background, opaque clean dog interior with antialiased edges.
Breed identity: broad strong head and muzzle, triangular natural folded ears, warm brown eyes, black nose, muscular compact adult dog with normal strong legs and paws, glossy short BLACK coat and rich RUST-TAN eyebrow spots, cheeks/muzzle sides, chest patches and lower legs. Recognizable Rottweiler, not a Labrador painted black, not a Doberman, not a puppy with a giant head. Natural undocked tail, no collar, friendly steady confident demeanor, animal not humanoid. Dark coat must retain soft charcoal/blue-grey highlights readable on both dark and light desktop backgrounds. Consistent markings and proportions throughout.
Layout is crucial: every entire dog fits INSIDE its own cell with at least 20 pixels clear margin on all four sides, including ears, toes and tail. Keep common drawing scale and consistent gentle three-quarter view facing right. Lowest paw y=230 within each cell. Modestly smaller than the reference dogs to ensure nothing clips. Four anatomically coherent paws, one natural tail. No detached elements.
Each row is four DISTINCT real illustrated animation poses, read left to right, first/last close enough for looping:
ROW1 idle: seated attentive dog, a relaxed blink and soft tail wag, stable body.
ROW2 thinking: seated curious head tilts, subtle folded-ear movement and focused gaze.
ROW3 working: stands and walks purposefully IN PLACE toward right, four proper alternating paw poses, fixed body center, tail gently following.
ROW4 waiting: calmly lying on its front paws, small eye shifts, slow blink and tiny ear twitch.
ROW5 done: happy playful bow, rises proudly and a small happy bounce, relaxed open mouth and wagging tail; all parts stay within cell.
ROW6 error: seated concerned head dip, folded ears lower slightly, apologetic blink; gentle, not frightened.
Pose changes must come from drawn head, ears, paws and tail rather than body squashing or stretching. Preserve consistent scale and crisp silhouettes. Output one final transparent PNG atlas only.
