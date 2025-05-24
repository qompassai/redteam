FROM archlinux

# Setup mirrors
RUN printf "[multilib]\nInclude = /etc/pacman.d/mirrorlist\n" \
        >> "$path/etc/pacman.conf" && \
    sed -i 's/^#Server/Server/' /etc/pacman.d/mirrorlist && \
    curl -s https://blackarch.org/strap.sh | bash -

RUN pacman --noconfirm --noprogressbar --needed -Syyu base-devel

RUN useradd -m -d /src -G wheel -g users builder -s /bin/bash && \
    echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    echo "root ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER builder

WORKDIR /src

COPY --chown=builder:users . .

ENTRYPOINT ["makepkg"]

CMD ["-s", "-f", "--noconfirm", "--needed", "--noprogressbar"]
