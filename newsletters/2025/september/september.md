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

- [**HBM4 is already be in its "E" form, spurred by Nvidia**](#hbm4-is-already-be-in-its-e-form-spurred-by-nvidia)

- [**"AI" SSDs: 100x the speed for reads, but how?**](#ai-ssds-100x-the-speed-for-reads-but-how)

- [**Other notable headlines**](#other-notable-headlines)

---

# This month's updates

## Rubin CPX: The GPU no-one saw coming

At the AI Infra summit earlier this month Nvidia took the world by surprise by revealing a new GPU outside of their existing roadmap, the Rubin CPX. unlike the more "general purpose" GPUs (AI accelerators) in their recent mainline such as the H100/200 and B200/300, the CPX is designed specifically for one purpose: prefill.

When inferencing an LLM, there are two distinct stages that occur, differentiated by their memory and compute requirements - prefill and decode. Prefill is the stage where the context window - all of the instructions, AI model memory, and additional pre-token generation information - is loaded onto the GPU, and decode is the stage where the new tokens are generated sequentially. This means that the prefill stage is compute-bound, as all the tokens from the context window are loaded once and can all be processed in parallel, needing much more compute than memory bandwidth.

The decode stage is the opposite, where each new token generated must use all or some of the previous tokens and must load the previously computed products from memory. Since the data computations are much faster than data movement, the decode stage is memory-bound, needing a high memory bandwidth rather than compute to maintain a high throughput.

The Rubin CPX doesn't optimise for prefill in speed but in cost, both in its purchasing price and its operating cost. To reduce the cost to the buyer, Nvidia replaced the fast but expensive HBM (high-bandwidth memory) with the much cheaper and slower GDDR7 (graphics DDR gen. 7) and moved from a complicated dual-die design to a simpler monolithic single-die design. Fitting in 128GB of memory, the CPX has a bandwidth of ~2 TB/s from a 512-bit bus at 32 Gbps, which is sufficient for prefill workloads. Using GDDR also means that the power draw drops, with some estimates putting it at ~880W, a little higher than the 800W of the H100 NVL variant.

The single GPU die can output 30 PFLOPs of FP4 compute, which now seems to come at a 3:2 sparsity instead of the original 2:1, and Nvidia will defiently find some way to justify this eventually. Regardless, at FP16 and FP8 - which almost everyone actually uses a mixture of for real inference workloads - the CPX might deliver 7.5 and 15 PFLOPs respectively, double what the B200 PCIe variant is rated for. Realistically, 

Rubin CPX GPU is a monolithic single-die design, departing from the dual-GPU chiplet architecture of Blackwell and regular Rubin SKUs.

Uses 128GB GDDR7 memory, not HBM; bandwidth ~2 TB/s on a 512-bit bus using 32 Gbps chips, yielding much lower cost than HBM-equipped GPUs.

30 PetaFLOPS of NVFP4 compute precision (dense); ~20 PF (dense) vs. 33 PF (dense) for dual-die R200.

Specialized for the context ("prefill") stage of large-scale AI inference, enabling efficient processing of context windows >1 million tokens.

4 integrated NVENC and NVDEC video engines, enabling long-format media (video) generative and analytic workloads.

Attention processing hardware tripled vs GB300 Blackwell Ultra, enabling up to 3x speedups in context/attention ops.

PCIe Gen6 (not NVLink) system interconnect; ConnectX-9 NICs for scale-out (1600G), not scale-up.

Estimated TDP per CPX chip/module ~800–880W. Advanced liquid cooling via sandwiched cold plate in each compute tray.

Rack module enables up to 8 CPX per compute tray; NVL144 CPX rack integrates 144 CPX, 72 Rubin, and 36 Vera CPUs.

Rubric Platform System Architecture
Vera Rubin NVL144 CPX platform features:

144 Rubin CPX GPUs (128GB GDDR7 each)

72 Regular Rubin GPUs (dual-die, 288GB HBM4 each)

36 Vera CPUs (88 ARM cores each)

100TB aggregate fast memory; 1.7 PB/s combined memory bandwidth.

8 ExaFLOPS total AI compute at NVFP4 precision; over 2x Vera Rubin NVL144 and 7.5x Blackwell GB300 NVL72 systems.

Total rack power budget ~370 kW; mandatory full liquid cooling in sandwiched configuration for density/thermal management.

Cableless midplane PCB design (Amphenol B2B connectors, 44-layer PCBs) for reliability, density, and assembly efficiency.

ConnectX-9 cards support 1600G scale-out networking; Spectrum6 switches deliver 102.4T switching and co-packaged optics.

Disaggregated Inference: Prefill vs. Decode
LLM Inference is split into two distinct hardware-optimized stages:

Prefill/Context: Compute-bound, needs max FLOPS (context ingestion, first token generation, codebase analysis, video analysis). Handled by CPX GPU.

Decode/Generation: Memory-bound, requires bandwidth/density for token generation (with large KV cache). Handled by regular Rubin HBM GPUs.

Disaggregation (PD separation) improves throughput, lowers system TCO, and enables specialized rack designs; throughput up to 6x for long-context workloads.

Technical & Manufacturing Insights
CPX is manufactured with conventional BGA packaging (no CoWoS, no chiplets), improving supply and BOM cost.

Bill of Materials for CPX is ~25% that of R200; offers ~60% of the compute at a fraction of cost – largely due to GDDR7 and single die.

HBM now accounts for ~51% BOM cost in high-end GPUs (GB300); GDDR7 cuts memory cost by up to 80% compared to HBM chips.

PCB design: 44-layer, PTH midplane PCB; PCB value per GPU increases from ~$400 (GB200) to ~$900 (VR200/CPX).

Advanced cooling hardware and cabinet design to accommodate power and density; industry-leading adoption of direct microchannel and sandwich cold plates.

Rack-level deployment allows for flexible scaling of context vs. decode nodes by adding CPX "sidecar" racks for customer-specific needs.

Full rack designs are mandatory for capable deployment; energy density and cooling requirements drive mandatory liquid cooling adoption worldwide (projected >35% liquid-cooled rack shipment share by 2030).

Industry Impact & Roadmap
Rubin CPX represents a major leap in specialized inference hardware, shifting economics and efficiency for LLM, code analysis, multimodal, video-gen workloads.

Competitive impact: rivals (AMD, Google TPU, AWS) must now build their own context-specialized CPUs/GPUs, delaying market parity and requiring full roadmap shifts.

CPX likely to be succeeded by future baseband and decode-specialized GPUs (potential for dedicated token-generation chips at extreme memory bandwidth).

GDDR7 demand is expected to surge; Samsung is forecasted to gain 1-2 years’ lead in GDDR7 supply/profit due to CPX and RTX Pro 6000 adoption; Hynix/Micron preoccupied with HBM4/E.

NVIDIA's roadmap, as of Sep 2025: Blackwell Ultra → Rubin/Rubin CPX (2026) → Rubin Ultra (2027, quad-die + HBM4E) → Feynman (2028).

Technical Features & Applications
NVFP4 format (NVIDIA's custom FP4): delivers ultra-low-precision AI compute, with high accuracy retention (≤1% degradation PTQ from FP8) and up to 2% accuracy gain in key tasks.

Ecosystem: CPX designed for full compatibility with NVIDIA AI Enterprise software stack, Nemotron multimodal inference, Dynamo full-stack orchestration for context/generation split workflows.

Handles: Hour-long 1M+ token video, multimodal and long-context chat, enterprise-scale code analysis, persistent memory agentic AI workloads.

Provides 30–50x ROI per $100M datacenter CAPEX, claimed by NVIDIA to yield $5B token revenue per rack CAPEX.

Power budgets and cabinet density push limits: each 1U compute tray supports 7040W and requires full liquid cooling and sandwich cold plates for reliability and minimal throttling.

| Model                        | Architecture         | Memory         | Bandwidth   | Compute (Dense/Sparse)      | Specialization         | Interconnect   | Power      |
|------------------------------|----------------------|----------------|-------------|-----------------------------|------------------------|----------------|------------|
| Rubin CPX                    | Monolithic, BGA      | 128GB GDDR7    | ~2TB/s      | 20PF dense, 30PF sparse     | Prefill (Context)      | PCIe Gen6      | 800–880W   |
| Rubin R200                   | Dual-die, CoWoS      | 288GB HBM4     | 20.5TB/s    | 33PF dense, 50PF sparse     | Decode/Token Gen       | NVLink 6       | ~1000W     |
| Blackwell Ultra B300/GB300   | Dual-die, CoWoS      | 288GB HBM3E    | 13TB/s      | 25PF dense, 40PF sparse     | Both (less specialized)| NVLink 5       | ~800–1000W |

Direct microchannel engraving on GPU cover plate, microchannel covers, liquid injection – each tested for Rubin CPX's high power densities (up to 2300W per GPU).

Industry consensus: magnetic levitation compression likely to be mainstream in 3-4 years; key suppliers (Danfoss, Hanbell, Magnetic Valley).

3D printing and biomimetic microchannel heat dissipation modules in prototype testing for packaging and thermal optimization.

Silicone oil immersion cooling now preferred over F-gas/fluorinated coolant in datacenter context; reliability and cost.

Cable-free midplane PCB architecture enables denser tray layouts, board-to-board Amphenol connectors, increased reliability, and improves servicing and build density.

Deployment, Scalability, and Configurations
CPX available as: full NVL144 CPX rack; dual rack (NVL144 + CPX); flexible CPX-only rack for dedicated context processing; PCIe deployment options possible but not confirmed.

Scalable ratio of CPX (context) vs. Rubin (decode) GPUs to optimize for customer workloads and budget.

Networking: ConnectX-9 NICs (1600G), Quantum-X800 InfiniBand, Spectrum-XGS Ethernet, co-packaged optics.

Easily attached CPX racks allow for future upgrade to massive-context processing without replacing existing Rubin/HBM infrastructure.

## Huawei's ascending roadmap - in a market free from Nvidia

## Nvidia trades with Intel: $5B in exchange for custom x86 CPUs

## HBM4 is already be in its "E" form, spurred by Nvidia

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
* []()

---

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)