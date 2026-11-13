# Happy Judge Entry

An entry for the make.fun competition "Make the AI judge happy".

## What it does

`main.py` copies the prepared image `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), byte for byte, and
verifies the copy's size before exiting. Every run writes identical bytes.

## The image

A small round robot shares a steaming mug of hot chocolate with a laughing
child on a windowsill at golden hour, string lights glowing, snow falling
outside the window. One warm, specific, happy moment.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
