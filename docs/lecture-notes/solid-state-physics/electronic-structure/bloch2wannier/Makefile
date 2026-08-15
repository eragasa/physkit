LATEXMK ?= latexmk
TARGET := main

.PHONY: all clean

all:
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error $(TARGET).tex

clean:
	$(LATEXMK) -C $(TARGET).tex
