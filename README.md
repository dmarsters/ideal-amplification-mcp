# Ideal Amplification MCP

**Jungian ideal/anima-animus formalized as parametric intensification toward archetypal maximum**

Companion brick to `shadow-complement-integration`, completing the tri-polar model of self.

## The Tri-Polar Self

```
Shadow (Denied) ←――― Persona (Expressed) ―――→ Ideal (Aspirational)
    Antipode              Current State           Archetypal Maximum
  "What I deny"        "What I am now"         "What I could become"
```

### Three Psychological Operations

1. **Shadow Complement** (via `shadow-complement-integration`)
   - Operation: Categorical antipode
   - Example: `gules → argent` (red flips to white)
   - Psychology: Acknowledging denied aspects creates wholeness

2. **Persona** (via `multi-domain-colimit-composer`)
   - Operation: Identity morphism
   - Example: `gules, weight=0.6` (current state)
   - Psychology: Authentic self-expression

3. **Ideal Amplification** (this brick)
   - Operation: Parametric intensification
   - Example: `gules → purer_gules, weight=0.6 → 0.8`
   - Psychology: Pursuing aspirational growth

## Installation

```bash
pip install -e .
```

## Architecture

### Three-Layer Olog Pattern

```
Layer 1: Categorical Structure (YAML olog)
├── Amplification rules by domain
├── Integration mode specifications
└── Intentionality principles

Layer 2: Deterministic Computation (0 tokens)
├── Continuous parameter extrapolation
├── Categorical archetypal selection
└── Three-way weighted blending

Layer 3: Claude Synthesis (~100-200 tokens)
└── Tri-polar psychological space interpretation
```

### Cost Profile

- **Deterministic operations**: 0 tokens
- **Claude synthesis**: ~100-200 tokens
- **Total savings**: ~70% vs pure LLM approach

## Usage

### Basic Ideal Amplification

```python
# Get current persona from colimit
persona = {
    "visual_weight": 0.6,
    "contrast_level": 0.7,
    "detail_density": 0.5
}

# Compute ideal amplification (push toward archetype)
result = compute_ideal_amplification(
    unified_parameters=json.dumps(persona),
    aesthetic_domain="heraldic_blazonry",
    amplification_level=0.5  # Halfway to archetype
)

# Result:
# {
#   "persona": {"visual_weight": 0.6, ...},
#   "ideal": {"visual_weight": 0.8, "contrast_level": 0.85, ...},
#   "amplification_level": 0.5,
#   "intentionality": "..."
# }
```

### Three-Way Integration (Shadow + Persona + Ideal)

```python
# Get all three poles
shadow = compute_shadow_complement(persona, ...)  # via shadow-complement-integration
persona = get_colimit_composition(...)            # via multi-domain-colimit-composer
ideal = compute_ideal_amplification(persona, ...)  # this brick

# Integrate all three
result = integrate_three_way(
    shadow_parameters=json.dumps(shadow),
    persona_parameters=json.dumps(persona),
    ideal_parameters=json.dumps(ideal),
    integration_mode="growth_emphasis"  # 10% shadow, 30% persona, 60% ideal
)

# Claude synthesizes from tri-polar space
```

### Integration Modes

```python
# List available modes
modes = list_amplification_modes()

# Modes:
# - balanced_wholeness: 25% shadow, 50% persona, 25% ideal
# - growth_emphasis: 10% shadow, 30% persona, 60% ideal
# - integration_emphasis: 40% shadow, 40% persona, 20% ideal
# - dynamic_tension: 33% each (maximum tension)
```

## Supported Domains

- `heraldic_blazonry`: Tincture purity, visual weight, contrast
- `jazz_improvisation`: Swing ratio, harmonic tension, virtuosity
- `cocktail_aesthetics`: Balance perfection, complexity, presentation
- `wine_tasting`: Acidity/tannin toward varietal archetype

Each domain has specific amplification rules in the olog.

## Examples

### Example 1: Personal Development Portrait

```python
# User: Software engineer who denies leadership qualities,
#       currently competent technical IC,
#       aspires to be architectural visionary

persona = {
    "technical_depth": 0.8,    # Strong technical skills
    "leadership_presence": 0.2, # Avoids leadership
    "vision_clarity": 0.5       # Decent but not exceptional
}

shadow = {
    "technical_depth": 0.2,     # Complement: Non-technical
    "leadership_presence": 0.8,  # What they deny!
    "vision_clarity": 0.5
}

ideal = {
    "technical_depth": 0.95,    # Amplified mastery
    "leadership_presence": 0.4,  # Slight increase (limited by denial)
    "vision_clarity": 0.85       # Amplified toward visionary
}

# Balanced integration shows:
# - Technical excellence (persona + ideal)
# - Hints of leadership capability (shadow acknowledgment)
# - Clear architectural vision (ideal amplification)
```

### Example 2: Brand Evolution Imagery

```python
# Brand: Craft brewery
# Shadow: What they avoid (mass-market appeal)
# Persona: Current state (local artisan)
# Ideal: Aspiration (respected regional icon)

# Growth emphasis mode (60% ideal) shows:
# - Current artisanal identity preserved
# - Subtle nods to broader accessibility
# - Strong push toward regional influence
```

### Example 3: Hero's Journey Visualization

```python
# Integration emphasis mode (40% shadow, 40% persona, 20% ideal)
# Shows character at crisis point:
# - Must integrate shadow (denied qualities)
# - Maintain core identity (persona)
# - Glimpse of potential (ideal)
```

## Tools

### Layer 1: Taxonomy Retrieval (0 tokens)

```python
list_amplification_modes()           # All integration modes
get_amplification_parameters(domain) # Domain-specific rules
get_intentionality_principles()      # Why this works
get_tri_polar_model()                # Complete model structure
```

### Layer 2: Computation (0 tokens)

```python
compute_ideal_amplification(
    unified_parameters,
    aesthetic_domain,
    amplification_level=0.3,
    amplification_focus=None  # Or list of parameters
)
```

### Layer 3: Integration (0 tokens + ~100-200 synthesis)

```python
integrate_three_way(
    shadow_parameters,
    persona_parameters,
    ideal_parameters,
    integration_mode="balanced_wholeness",
    custom_weights=None  # Or {"shadow": 0.2, "persona": 0.5, "ideal": 0.3}
)
```

### Analysis Tools

```python
compare_shadow_vs_ideal(persona, shadow, ideal)
suggest_integration_strategy(use_case, emphasis_preference)
```

## Integration with Lushy Ecosystem

### Companion Bricks

```
multi-domain-colimit-composer
    ↓ (provides persona)
    ├── shadow-complement-integration (computes shadow)
    └── ideal-amplification-mcp (computes ideal)
        ↓
    integrate_three_way
        ↓
    Claude synthesis
```

### Typical Workflow

1. User provides multi-domain intent
2. `multi-domain-colimit-composer` creates unified persona
3. `shadow-complement-integration` computes antipodal shadow
4. `ideal-amplification-mcp` computes archetypal ideal
5. `integrate_three_way` blends all three poles
6. Claude synthesizes from tri-polar psychological space

## Mathematical Foundation

### Categorical Structure

```
Shadow Complement: F_shadow: Persona → Antipode
  Operation: Categorical flip (gules ↔ argent)

Ideal Amplification: F_ideal: Persona → Archetype
  Operation: Parametric extrapolation (gules → purer_gules)

Three-Way Integration: F_tri: (Shadow, Persona, Ideal) → Blended_Self
  Operation: Weighted colimit (α·S + β·P + γ·I where α+β+γ=1)
```

### Intentionality

**Why parametric intensification works:**

1. **Archetypal recognition**: Humans instantly recognize "most X" versions
2. **Growth aesthetic**: Images showing becoming create engagement
3. **Identity preservation**: Amplifying same direction maintains coherence

## Testing

```bash
pytest tests/ -v
```

Test coverage:
- Taxonomy retrieval (Layer 1)
- Amplification computation (Layer 2)
- Three-way integration (Layer 3)
- Constraint validation
- Domain-specific rules

## Claude Desktop Configuration

```json
{
  "mcpServers": {
    "ideal-amplification": {
      "command": "python",
      "args": [
        "-m",
        "ideal_amplification_mcp.server"
      ],
      "env": {
        "PYTHONPATH": "/path/to/ideal-amplification-mcp/src"
      }
    }
  }
}
```

## License

Part of the Lushy epistemological infrastructure platform.

## Contact

Dal Marsters - dal@lushy.app

---

**Companion to shadow-complement-integration**  
**Part of the Lushy three-layer olog architecture**  
**Version 1.0**
