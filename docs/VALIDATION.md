# Validation principles

Separate four states: **PLANNED**, **BUILT**, **TESTED ON HOST**, and **VERIFIED ON TV**.

A server-side HTTP 200 or successful JavaScript syntax check does not establish LG TV playback. A reachable TCP port does not demonstrate SSH authentication or functional UI operation.

When recording a device test, capture:

1. Device generation, OS revision and build identification (excluding unique device identifiers).
2. Exact manual or automated test procedure.
3. Video startup behavior, remote Back/Exit and fullscreen behavior.
4. CPU and memory measurements under identical conditions.
5. Codec, stream resolution and whether decoding was demonstrably hardware-accelerated.
6. Reproducibility and observed failures.

Until independently repeated on actual hardware, 4K/HDR, media-pipeline reliability and remote-control fixes remain unverified in this public project.
