[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# September 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/september/images/title.jpeg)

*Will those of us born today be able to live without AI? Given how much of humanity now exists in a state of dependence on technology in some way or the other, and the subset of that population that is dependent on their smartphones, it's natural to think that a much smaller but rapidly growing subset is now dependent on AI-powered tools. Is that the ultimate plan for those who develop our AI models? To create a world in which AI is absolutely necessary, making their existence also, absolutely necessary?*

This is the SixRackUnits AI hardware newsletter, keeping you up to date with the latest in AI hardware, datacentre technology, and the future of compute. With a field changing this fast, staying on top of everything, or even summarising all the material available can be difficult - so we do it for you.

For a space to share sources and news/updates, join our telegram channel <a href="https://t.me/aihpc_infra_fans">here</a> or if you like short form posts on similar topics, check out the <a href="https://sixrackunits.substack.com/notes">notes</a> section of this newsletter or my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a>.

[**This month's updates:**](#this-months-updates)

- [**Rubin CPX: The GPU no-one saw coming**](#rubin-cpx-the-gpu-no-one-saw-coming)

- [**Huawei's ascending roadmap - in a market free from Nvidia**](#huaweis-ascending-roadmap---in-a-market-free-from-nvidia)

- [**Nvidia trades with Intel: $5B in exchange for custom x86 CPUs**](#nvidia-trades-with-intel-5b-in-exchange-for-custom-x86-cpus)

- [**HBM4 is evolving before it's even here, spurred by Nvidia**](#hbm4-is-evolving-before-its-even-here-spurred-by-nvidia)

- [**"AI" SSDs: 100x the speed for reads, but how?**](#ai-ssds-100x-the-speed-for-reads-but-how)

- [**Other notable headlines**](#other-notable-headlines)

---

# This month's updates

## Rubin CPX: The GPU no-one saw coming

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/september/images/cpx_chip.png)

*Source: Nvidia*

At the [AI Infra summit](https://www.ai-infra-summit.com/events/ai-infra-summit) earlier this month Nvidia took the world by surprise by revealing a new GPU outside of their existing roadmap, the [Rubin CPX](https://developer.nvidia.com/blog/nvidia-rubin-cpx-accelerates-inference-performance-and-efficiency-for-1m-token-context-workloads/). Unlike the more "general purpose" GPUs (AI accelerators) in their recent mainline such as the H100/200 and B200/300, the CPX is designed specifically for one purpose: prefill.

When inferencing an LLM, there are [two distinct stages](https://www.theregister.com/2025/09/10/nvidia_rubin_cpx/#:~:text=The%20problem%20in%20context) to run, differentiated by their memory and compute requirements: prefill, decode. Prefill is the stage where the context window - all of the instructions, AI model memory, and additional pre-token generation information - is loaded onto the GPU, and decode is the stage where the new tokens are then generated sequentially. This means that the prefill stage is compute-bound, as all the tokens from the context window are loaded once and can all be processed in parallel, needing much more compute than memory bandwidth.

The decode stage is the opposite, where each new token generated must use all or some of the previous tokens and must load the previously computed products from memory. Since computations are much faster than data movement, the decode stage is memory-bound, needing a high memory bandwidth rather than compute to maintain a high throughput.

The Rubin CPX doesn't optimise for prefill in speed but in cost, both in its price and its energy efficiency. To reduce the cost to the buyer, Nvidia replaced the fast but expensive HBM (high-bandwidth memory) with the much [cheaper but slower](https://semianalysis.com/2025/09/10/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack/#:~:text=Switching%20from%20using%20HBM%20to,of%20memory%20bandwidth%20per%20R200.) GDDR7 (graphics DDR gen. 7). Fitting in 128GB of memory, the CPX has a bandwidth of ~2 TB/s from a 512-bit bus at 32 Gbps, which is sufficient for prefill workloads. Using GDDR also means that the power draw drops, with SemiAnalysis' estimates putting it at ~880W, a little higher than the 800W of the H100 NVL variant.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/september/images/cpx_tray_rack.png)

*Source: Nvidia*

As well as the simpler memory, the CPX also uses a simpler design, moving from a complicated dual-die chiplet-based design like the [blackwell series did](https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)) to a simpler monolithic single-die design. In addition, Nvidia also decided to stick to the PCIe gen 6. for the D2D (device-to-device) interconnect instead of the far more expensive NVLink, as a prefill/inferencing focused GPU wouldn't need the higher bandwidth and complexity of NVLink. Both of these decisions make the CPX easier to manufacture and hence cheaper yet.

Despite the seemingly light-weight design, there are two significant upgrades: increased video encode/decode capacity and triple the number (or throughput) of transformer engines. NVENC/NVDEC engines handle processing functions for video, an increasingly popular and particularly demanding modality for AI models. The transformer engines handle mixed precision attention operations and accelerate the computationally heavy prefill stage significantly.

All in all, the CPX should output [30 PFLOPs of FP4 compute](https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference), which now seems to come at a [3:2 sparsity](https://semianalysis.com/2025/09/10/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack/#:~:text=follow%20the%20same-,3%3A2%20sparse,-to%20dense%20ratio) ratio instead of the original 2:1, something Nvidia will definitely find some way to justify eventually. Regardless, at FP16 and FP8 - which almost everyone actually for real inference workloads - the CPX might deliver 7.5 and 15 PFLOPs respectively, double what the B200 PCIe variant is rated for.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/september/images/cpx_racks.png)

*Source: SemiAnalysis*

Keeping in line with their focus on rack-scale systems, Nvidia also announced [two new rack SKUs](https://www-nextplatform-com.cdn.ampproject.org/c/s/www.nextplatform.com/2025/09/11/nvidia-disaggregates-long-context-inference-to-drive-bang-for-the-buck/amp/#:~:text=Here%20are%20the%20feeds%20and%20speeds%20for%20the%20Vera%20Rubin%20NVL144%20rackscale%20system%3A), the VR200 NVL144 CPX and the VR CPX. The first builds upon the already announced NVL144 "Oberon" rack design, similar to the existing GB200/300 NVL72 designs, but now adds 8 Rubin CPX GPUs per compute tray, totalling to an 144 additional GPUs in the system. This brings the total estimated power of such a deployment up from ~225kW to ~370kW for a single rack - a number difficult for most datacentres to even imagine.

The second, CPX-only rack is a more compact and sensible option, sticking to 144 CPX's per rack but with no R200 GPUs or NVLink spine. This still comes in at ~190kW per rack, but is still more manageable for hyperscalers and research labs that have planned for 200-220kW racks over the comings months. This can act as a sidecar even for the now decode focused HBM-heavy VR200 systems, connected over the CX-9 + 1.6T Ethernet/InfiniBand scale-out fabrics.

There's a lot more to say on this topic around the compute tray architecture and cooling systems too, but for more on this, [SemiAnalysis](https://semianalysis.com/2025/09/10/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack/) is currently the best source.

## Huawei's ascend roadmap - in a market free from Nvidia

## Nvidia trades with Intel: $5B in exchange for custom x86 CPUs

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/september/images/intel_nvidia_logos.jpg)

*Source: Nvidia*

To some, this is old news. It's been confirmed now that for over a year, Nvidia and Intel have had [three separate teams](https://www.tomshardware.com/pc-components/cpus/teams-at-nvidia-and-intel-have-been-working-in-secret-on-jointly-developed-processors-for-a-year-the-trump-administration-has-no-involvement-in-this-partnership-at-all) collaborating in secret on joint designs for processors, AI PCs, and datacentre servers. However it all came to light earlier this month when both parties [officially announced](https://nvidianews.nvidia.com/news/nvidia-and-intel-to-develop-ai-infrastructure-and-personal-computing-products) the long-term partnership with Nvidia committing to investing $5B in Intel through a stock purchase.

Investors expressed confidence in both parties through the stocks of two sides seeing significant increases within the day, Intel's being far sharper at an almost 30% increase. For GPU servers on the market now, Intel CPUs have seen a [decline in market share](https://www.techpowerup.com/338409/intels-server-share-slips-to-67-as-amd-and-arm-widen-the-gap) of the past few years with AMD making a steady rise, though with their upcoming Granite rapids processors this might change.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/september/images/intel_nvidia_dgx_default.jpg)

*Source: Intel*

For a while now, Both [Intel](https://newsroom.intel.com/de/artificial-intelligence/new-intel-xeon-6-cpus-maximize-gpu-ai-performance) and [Nvidia](https://resources.nvidia.com/en-us-dgx-software/dgx-b300-datasheet) have been pushing the higher end [Granite rapids 6776P](https://www.intel.com/content/www/us/en/products/sku/243691/intel-xeon-6776p-processor-336m-cache-2-30-ghz/specifications.html) 64-core (128 threads) CPU as *the* CPU for Nvidia's official 8-GPU DGX servers. Intel CPUs have been extensively studied and optimised in the more common, non-DGX 4 and 8 GPU servers too, which are aimed at hyperscalers and neoclouds. Many of these compute providers have optimised their software and platforms taking Intel and Nvidia as the default.

The largest victims of this partnership therefore [are AMD and ARM](https://www.youtube.com/watch?v=vvlE8-MzxyA) - both suffering from negative investor sentiment towards their future in AI servers. At least [until the end of the Rubin-era](https://www.nextplatform.com/2025/03/19/nvidia-draws-gpu-system-roadmap-out-to-2028/), Nvidia has committed to using "Vera" ARM-based CPUs, the successor to their popular "Grace" CPUs pushed with their NVL rack-scale systems. Given that this collaboration with Intel will bear fruit around 2027/28, it's possible that Nvidia will offer x86 alternatives to the ARM CPUs in their NVL cabinets, or maybe just default to Intel CPUs entirely.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/september/images/intel_nvidia_grace_boards.jpg)

*Source: Nvidia*

AMD, whose CPUs have already suffered with [minor performance issues](https://semianalysis.substack.com/p/ai-neocloud-playbook-and-anatomy#:~:text=we%20recommend%20using%20Intel%20CPUs%20as%20on%20Intel%20it%20is%20easier%20to%20get%20NCCL%20performance%20correct) in Nvidia GPU servers according to SemiAnalysis' testing, may have a difficult time competing. Currently, the previously mentioned vendors/integrators offer AMD versions of the popular 8-GPU HGX systems, though with Intel CPUs becoming highly optimised and tightly integrated with Nvidia GPUs in the coming years, this may prove to become a difficult sell.

This tight integration might result in a number of useful features for future DGX/NVL servers:

- NVLink integration: Putting 1.8/3.6 TB/s BIDI links for CPU-CPU or CPU-GPU, without needing to recompile anything for ARM ISAs
- power-sloshing: Dynamic frequency scaling not just between cores on a CPU, but also between the GPU and CPU to balance power and performance where needed
- Variety for host memory: Making a variety of memory technologies available for the CPU from LPDDR (low power DDR) for energy efficiency to MRDIMMs (multi-rank DIMMs) for capacity
- Using Intel's AMX (Advanced Matrix Extensions): Allowing x86 Intel CPUs to make more use of AMX with optimised I/O and shared memory spaces between devices on the board

## HBM4 is evolving before it's even here, spurred by Nvidia

The development and progression of HBM is now controlled not by the big three manufacturers (Samsung, SK Hynix, Micron) but by Nvidia, who has shown that they can just [make demands](https://x.com/Jukanlosreve/status/1966061623061381256) as they like and the suppliers will bend to their will. Originally targeting 8Gbps per pin according to JEDEC standards, Nvidia asked their HBM suppliers to raise the speeds to 9, and [then eventually 11Gbps](https://x.com/Jukanlosreve/status/1965960343974470126) - because they could.

![https://x.com/Jukanlosreve/status/1965961127566962885](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/september/images/hbm_tweet.png)

*Source: Jukan (@jukanlosreve on X)*

Initially Samsung [met the request](https://www.tweaktown.com/news/107669/nvidia-asked-for-9gbps-on-hbm4-then-for-10-11gbps-samsungs-hbm4-looks-superior-for-10gbps-plus/index.html) head on by promising to hit 10Gbps over each of the 2048 pins, resulting a per-module bandwidth of just over 2.5TB/s. Supporting up to 12 layers in its current implementations, each consisting of 24Gb, this means each 36GB of memory can independently be moved back and forth at that theoretical peak bandwidth. All three manufacturers intend to hit 32Gb capacity per layer and 16 layers in a stack at the same bandwidth (for now), meaning that by the end of 2026, there should be at least three independent implementations of 64GB HBM4 modules.

SK-Hynix being the now dominant HBM manufacturer also claimed that it would reach the target, though more recently may have exceeded that rate too. Micron meanwhile waited a little and then [made headlines](https://www.trendforce.com/news/2025/09/24/news-micron-counters-hbm4-speed-doubts-with-11-gbps-custom-hbm4e-due-2027-with-higher-margins/) by allegedly reaching over 11Gbps, a remarkable number currently under scrutiny as they intend to use the same process node as they use for DRAM for producing their logic dies in house.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/september/images/hbm_micron.png)

*Source: Micron*

The logic die controls how the memory is moved to and from the pins connecting to the rest of the chip, as well as many other functions such as ensuring signal integrity and managing error correction. Producing these logic die with a process node optimised for DRAM would naturally result in suboptimal performance, or at least that's what [analysts fear](https://x.com/Jukanlosreve/status/1966362636360286250) after hearing Micron's claims.

To summarise the specs of upcoming implementations ([1](https://www.tomshardware.com/micron-hands-tsmc-the-keys-to-hbm4e) [2](https://www.trendforce.com/news/2025/09/24/news-micron-counters-hbm4-speed-doubts-with-11-gbps-custom-hbm4e-due-2027-with-higher-margins/) [3](https://www.allpcb.com/allelectrohub/3d-dram-roadmap-and-production-timeline)):
| Vendor/Tech        | DRAM Node (nm) | Base Die Process (nm)   | Bonding Stack/Method                                   | Max Speed (Gbps)          | Max Stack (Hi) | Key Notes                                                 |
|--------------------|---------------|-------------------------|--------------------------------------------------------|---------------------------|----------------|-----------------------------------------------------------|
| Samsung HBM4       | 12 (1c)       | 4 (Samsung Foundry)     | TC-NCF (Thermal Compression Non-Conductive Film), Hybrid Bond | 10–11 (target)            | 16             | 4nm logic base, EUV equipped, advanced hybrid bonding      |
| SK Hynix HBM4      | 13 (1b), ramping to 12 (1c) | 3 (TSMC N3)            | MR-MUF (Mass Reflow Molded Underfill), Hybrid Bond     | >10 (demo, 10.4–11)       | 16             | TSMC N3 logic base die, MR-MUF DRAM stacking               |
| Micron HBM4        | 12.2 (1β)     | 12.2 (DRAM-based logic) | Standard bonding (classic DRAM stack), limited hybrid  | >11 (claimed, contested)  | 16             | Logic in DRAM node; not external logic node like Samsung/SKH|

## "AI" SSDs: 100x the speed for reads, but how?

---

## Other notable headlines

* [Chinese tech giants Alibaba and Baidu have custom silicon in use - competitive with Nvidia H20s](https://x.com/Jukanlosreve/status/1966289098081181715)
* [Trading firm XTX Markets open sources their exabyte scale, multi-region distributed filesystem, TernFS](https://www.xtxmarkets.com/tech/2025-ternfs/)
* [Tesla might make its next custom silicon using Intel's 18A process](https://www.tweaktown.com/news/107721/tesla-rumored-to-make-an-ai-chip-for-its-evs-on-the-intel-18a-process-node/index.html)
* [NVidia considering TSMC's A16 for its Feynman architecture GPUs for 2028](https://www.trendforce.com/news/2025/09/15/news-nvidia-may-be-among-the-first-to-adopt-tsmc-a16-for-2028-feynman-architecture/)
* [Chinese government bans tech firms from buying Nvidia, forcing the use of domestic hardware](https://www.ft.com/content/12adf92d-3e34-428a-8d61-c9169511915c)
* [Broadcom to devleop OpenAI's custom ASIC - Titan XPU](https://www-nextplatform-com.cdn.ampproject.org/c/s/www.nextplatform.com/2025/09/05/broadcom-lands-shepherding-deal-for-openai-titan-xpu/amp/)
* [NVidia cancels SOCAMM, moving on to SOCAMM2 for Rubin - soldering LPDDRXX for now](https://x.com/Jukanlosreve/status/1967145562966544733)
* [Alibaba releases a demo of their Panjiu-series fully liquid-cooled 128 GPU SuperNode at their annual ASPARA conference](https://x.com/semivision_tw/status/1971114184005071175)
* [Nvidia promises it will buy double Samsung's current total GDDR7 production - likely to supply their RTX and CPX series GPUs](https://www.tweaktown.com/news/107618/nvidia-requests-samsung-to-double-its-gddr7-production-well-double-the-order-so-be-ready/index.html)

---

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)