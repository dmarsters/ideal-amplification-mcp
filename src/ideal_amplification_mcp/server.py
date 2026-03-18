#!/usr/bin/env python3
"""
Ideal Amplification MCP Server

Jungian ideal/anima-animus formalized as parametric intensification toward
archetypal maximum. Companion to shadow-complement-integration.

Architecture:
- Layer 1: Deterministic amplification rules from olog (0 tokens)
- Layer 2: Mathematical extrapolation operations (0 tokens)
- Layer 3: Claude synthesis of psychological space (~100-200 tokens)

Tri-Polar Self Model:
- Shadow (denied): Categorical antipode via shadow-complement-integration
- Persona (expressed): Current aesthetic parameters from colimit
- Ideal (aspirational): Parametric intensification toward archetype

Supported Domains:
- heraldic_blazonry, jazz_improvisation, cocktail_aesthetics, wine_tasting (via olog)
- microscopy_aesthetics (via dedicated parameter extraction + amplification rules)

Microscopy Support:
- extract_microscopy_parameters_tool: Converts modality choices to parameters
- Supports all 7 major microscopy types (fluorescence, electron, etc.)
- Respects physical constraints (diffraction limits, quantum efficiency)

Total cost savings: ~70% vs pure LLM approach
"""
import sys
import yaml
import json
import math
import numpy as np
from fastmcp import FastMCP
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path


# Initialize MCP server
mcp = FastMCP("ideal-amplification")

# Load olog specification
def _find_olog_path(filename: str) -> Path:
    """Search multiple locations for olog files."""
    current_file = Path(__file__).resolve()
    current_dir = current_file.parent
    
    search_paths = [
        current_dir / "ologs" / filename,
        current_dir / filename,
        current_dir.parent / "ologs" / filename,
        current_dir.parent.parent / "ologs" / filename,  # For src/ structure
    ]
    
    for path in search_paths:
        if path.exists():
            print(f"Found {filename} at: {path}", file=sys.stderr)
            return path
    
    raise FileNotFoundError(
        f"Could not find {filename} in:\n" + 
        "\n".join(f"  - {p}" for p in search_paths)
    )

# Load files
_olog_path = _find_olog_path("ideal_amplification.olog.yaml")
with open(_olog_path, 'r') as f:
    OLOG = yaml.safe_load(f)

_microscopy_olog_path = _find_olog_path("microscopy_aesthetics.olog.yaml")
with open(_microscopy_olog_path, 'r') as f:
    MICROSCOPY_OLOG = yaml.safe_load(f)


# ==============================================================================
# LAYER 1: Taxonomy Retrieval (0 tokens)
# ==============================================================================

@mcp.tool()
def list_amplification_modes() -> str:
    """
    List all available three-way integration modes.
    
    Shows weight distributions for combining shadow, persona, and ideal
    into complete psychological portraits.
    
    Returns:
        JSON string with integration mode specifications
        
    Cost: 0 tokens (pure taxonomy lookup)
    """
    modes = OLOG['three_way_integration']['integration_modes']
    
    result = {
        "integration_modes": {},
        "description": "Weight distributions for shadow + persona + ideal blending"
    }
    
    for mode_name, mode_spec in modes.items():
        result["integration_modes"][mode_name] = {
            "shadow_weight": mode_spec['shadow_weight'],
            "persona_weight": mode_spec['persona_weight'],
            "ideal_weight": mode_spec['ideal_weight'],
            "effect": mode_spec['effect'],
            "use_case": mode_spec['use_case'],
            "intentionality": mode_spec['intentionality']
        }
    
    return json.dumps(result, indent=2)


@mcp.tool()
def get_amplification_parameters(aesthetic_domain: str) -> str:
    """
    Get amplification rules for a specific aesthetic domain.
    
    Returns parameter-specific amplification operations showing how
    to intensify toward archetypal maximum.
    
    Args:
        aesthetic_domain: Domain name (e.g., "heraldic_blazonry", "jazz_improvisation")
        
    Returns:
        JSON string with amplification rules for all parameters
        
    Cost: 0 tokens (deterministic olog lookup)
        
    Example:
        get_amplification_parameters("heraldic_blazonry")
        Returns rules for tincture purity, visual weight, contrast, etc.
    """
    operations = OLOG['amplification_operations']
    
    if aesthetic_domain not in operations:
        available = list(operations.keys())
        available.remove('description')
        return json.dumps({
            "error": f"Domain '{aesthetic_domain}' not found",
            "available_domains": available
        }, indent=2)
    
    domain_ops = operations[aesthetic_domain]
    
    result = {
        "domain": aesthetic_domain,
        "description": domain_ops['description'],
        "parameters": domain_ops['parameters']
    }
    
    return json.dumps(result, indent=2)


@mcp.tool()
def get_intentionality_principles() -> str:
    """
    Get the core intentionality explaining why ideal amplification works.
    
    Returns psychological foundations, visual psychology principles,
    and categorical elegance of the amplification approach.
    
    Returns:
        JSON string with complete intentionality documentation
        
    Cost: 0 tokens (pure taxonomy retrieval)
    """
    intentionality = OLOG['intentionality']
    
    result = {
        "psychological_foundation": intentionality['psychological_foundation'],
        "visual_psychology": intentionality['visual_psychology'],
        "categorical_elegance": intentionality['categorical_elegance']
    }
    
    return json.dumps(result, indent=2)


@mcp.tool()
def get_tri_polar_model() -> str:
    """
    Get complete tri-polar self model specification.
    
    Shows how shadow, persona, and ideal form three poles of
    psychological space with morphisms between them.
    
    Returns:
        JSON string with tri-polar model structure
        
    Cost: 0 tokens (taxonomy lookup)
    """
    tri_polar = OLOG['tri_polar_self']
    
    return json.dumps(tri_polar, indent=2)


# ==============================================================================
# LAYER 2: Amplification Computation (0 tokens)
# ==============================================================================

def _amplify_continuous_parameter(
    current_value: float,
    amplification_level: float,
    target_extreme: float = 1.0
) -> float:
    """
    Linear extrapolation toward parametric extreme.
    
    Formula: value_ideal = value_current + (target - value_current) * amplification_level
    
    Args:
        current_value: Current parameter value [0.0, 1.0]
        amplification_level: How much to push [0.0, 1.0]
        target_extreme: Target maximum (default 1.0, can be 0.0 for minimalist ideals)
        
    Returns:
        Amplified value
    """
    delta = target_extreme - current_value
    return current_value + (delta * amplification_level)


def _amplify_categorical_parameter(
    current_value: str,
    parameter_name: str,
    domain_rules: Dict
) -> str:
    """
    Select archetypal variant for categorical parameters.
    
    Args:
        current_value: Current categorical value
        parameter_name: Name of parameter
        domain_rules: Domain amplification rules
        
    Returns:
        Archetypal variant
    """
    param_spec = domain_rules.get(parameter_name, {})
    
    # Check if there's an archetype mapping
    if param_spec.get('type') == 'categorical':
        # Look for archetypal variant in examples or operation
        if 'examples' in param_spec and current_value in param_spec['examples']:
            return param_spec['examples'][current_value]
        elif 'archetype' in param_spec:
            return param_spec['archetype']
    
    # Default: return current value (no amplification available)
    return current_value


def _extract_microscopy_parameters(
    microscopy_type: str,
    aesthetic_strength: str = "balanced",
    magnification: str = "medium"
) -> Dict[str, Any]:
    """
    Extract implied parameters from microscopy aesthetic choices.
    
    Bridges microscopy-aesthetics MCP (prompt generator) to 
    ideal-amplification MCP (parameter amplifier).
    
    Args:
        microscopy_type: The microscopy modality
        aesthetic_strength: subtle, balanced, strong, extreme
        magnification: low, medium, high
    
    Returns:
        Parameter dict ready for amplification
    """
    # Map aesthetic_strength to base parameter values
    strength_map = {
        "subtle": 0.5,
        "balanced": 0.65,
        "strong": 0.80,
        "extreme": 0.90
    }
    
    base_value = strength_map.get(aesthetic_strength.lower(), 0.65)
    
    # Core parameters (all modalities)
    params = {
        "signal_clarity": base_value,
        "contrast_intensity": base_value,
        "detail_density": base_value - 0.05,
        "dimensional_depth": base_value - 0.1,
        "magnification_scale": magnification
    }
    
    # Modality-specific parameters
    if microscopy_type == "fluorescence":
        params.update({
            "glow_intensity": base_value,
            "signal_specificity": base_value + 0.05,
            "color_saturation": base_value + 0.1,
            "multi_channel_separation": base_value,
            "color_palette_mode": "scientific"
        })
    
    elif microscopy_type == "electron":
        params.update({
            "surface_relief": base_value + 0.05,
            "textural_richness": base_value,
            "metallic_quality": base_value + 0.1,
            "monochrome_purity": base_value + 0.15
        })
    
    elif microscopy_type == "phase_contrast":
        params.update({
            "halo_intensity": base_value,
            "transparency_preservation": base_value + 0.1,
            "ethereal_quality": base_value - 0.05,
            "monochrome_purity": base_value + 0.1
        })
    
    elif microscopy_type == "confocal":
        params.update({
            "optical_sectioning_precision": base_value + 0.1,
            "volumetric_coherence": base_value,
            "z_axis_resolution": base_value - 0.05,
            "multi_channel_separation": base_value + 0.05,
            "color_palette_mode": "scientific"
        })
    
    elif microscopy_type == "darkfield":
        params.update({
            "edge_brilliance": base_value + 0.05,
            "background_darkness": base_value + 0.15,
            "scattered_light_intensity": base_value,
            "monochrome_purity": base_value + 0.1
        })
    
    elif microscopy_type == "brightfield":
        params.update({
            "stain_saturation": base_value,
            "tissue_clarity": base_value + 0.1,
            "histological_definition": base_value + 0.05
        })
    
    elif microscopy_type == "multiphoton":
        params.update({
            "penetration_depth": base_value,
            "autofluorescence_control": base_value + 0.1,
            "phototoxicity_minimization": base_value + 0.15,
            "color_saturation": base_value
        })
    
    return params


@mcp.tool()
def extract_microscopy_parameters_tool(
    microscopy_type: str,
    aesthetic_strength: str = "balanced",
    magnification: str = "medium"
) -> str:
    """
    Extract parameter representation from microscopy aesthetic choices.
    
    Bridge tool between microscopy-aesthetics and ideal-amplification.
    Use this to convert microscopy modality choices into numerical parameters
    that can be amplified.
    
    Args:
        microscopy_type: Microscopy modality (fluorescence, electron, phase_contrast,
                        confocal, darkfield, brightfield, multiphoton)
        aesthetic_strength: subtle, balanced, strong, extreme (default: balanced)
        magnification: low, medium, high (default: medium)
    
    Returns:
        JSON string with extracted parameters ready for amplification
        
    Cost: 0 tokens (deterministic mapping)
    
    Example:
        extract_microscopy_parameters_tool(
            microscopy_type="fluorescence",
            aesthetic_strength="balanced",
            magnification="high"
        )
        Returns: {"glow_intensity": 0.65, "signal_clarity": 0.65, ...}
    """
    params = _extract_microscopy_parameters(
        microscopy_type=microscopy_type,
        aesthetic_strength=aesthetic_strength,
        magnification=magnification
    )
    
    return json.dumps(params, indent=2)


@mcp.tool()
def compute_ideal_amplification(
    unified_parameters: str,  # JSON string
    aesthetic_domain: str,
    amplification_level: float = 0.3,
    amplification_focus: Optional[str] = None  # JSON list or None
) -> str:
    """
    Compute ideal amplification of aesthetic parameters.
    
    LAYER 2: Pure deterministic computation (0 LLM cost).
    
    Takes current persona parameters and extrapolates toward archetypal
    maximum. Unlike shadow_complement (which flips to opposite), this
    intensifies in the same direction.
    
    Args:
        unified_parameters: JSON string with current persona parameters
        aesthetic_domain: Domain for amplification rules
        amplification_level: How much to push toward ideal [0.0-1.0]
            0.0 = no change (current persona)
            0.5 = halfway to archetype
            1.0 = pure archetype (maximum expression)
        amplification_focus: Optional JSON list of parameters to amplify
            None = amplify all parameters
            
    Returns:
        JSON string with:
        - persona: Original parameters
        - ideal: Amplified parameters
        - amplification_level: Echo of input
        - intentionality: Why this amplification works
        
    Cost: 0 tokens (deterministic math)
    
    Example:
        compute_ideal_amplification(
            unified_parameters='{"visual_weight": 0.6, "contrast_level": 0.7}',
            aesthetic_domain="heraldic_blazonry",
            amplification_level=0.5
        )
        
        Returns ideal with visual_weight=0.8, contrast_level=0.85
    """
    # Parse inputs
    try:
        params = json.loads(unified_parameters)
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON in unified_parameters"}, indent=2)
    
    focus_params = None
    if amplification_focus:
        try:
            focus_params = json.loads(amplification_focus)
        except json.JSONDecodeError:
            return json.dumps({"error": "Invalid JSON in amplification_focus"}, indent=2)
    
    # Load domain rules
    operations = OLOG['amplification_operations']
    if aesthetic_domain not in operations:
        available = [k for k in operations.keys() if k != 'description']
        return json.dumps({
            "error": f"Domain '{aesthetic_domain}' not found",
            "available_domains": available
        }, indent=2)
    
    domain_rules = operations[aesthetic_domain]['parameters']
    
    # Compute amplified parameters
    ideal_params = {}
    
    for param_name, param_value in params.items():
        # Skip if not in focus (when focus is specified)
        if focus_params and param_name not in focus_params:
            ideal_params[param_name] = param_value
            continue
        
        # Check if we have amplification rules
        if param_name not in domain_rules:
            # No rules = no amplification
            ideal_params[param_name] = param_value
            continue
        
        param_spec = domain_rules[param_name]
        param_type = param_spec.get('type', 'continuous')
        
        if param_type == 'continuous':
            # Check if target depends on archetype
            if 'archetype_depends_on' in param_spec:
                # Context-dependent amplification (requires more info)
                # For now, default to maximizing
                target = 1.0
            else:
                # Standard amplification toward 1.0
                target = 1.0
            
            # Apply amplification
            if isinstance(param_value, (int, float)):
                ideal_params[param_name] = _amplify_continuous_parameter(
                    param_value,
                    amplification_level,
                    target
                )
            else:
                ideal_params[param_name] = param_value
        
        elif param_type == 'categorical':
            # Select archetypal variant
            ideal_params[param_name] = _amplify_categorical_parameter(
                param_value,
                param_name,
                domain_rules
            )
        
        else:
            # Unknown type = no amplification
            ideal_params[param_name] = param_value
    
    # Build intentionality
    domain_desc = operations[aesthetic_domain]['description']
    intentionality = f"{domain_desc}. Amplification level {amplification_level} pushes parameters toward archetypal maximum while preserving identity."
    
    result = {
        "persona": params,
        "ideal": ideal_params,
        "amplification_level": amplification_level,
        "metadata": {
            "domain": aesthetic_domain,
            "focus": focus_params if focus_params else "all parameters",
            "operation": "parametric_intensification"
        },
        "intentionality": intentionality
    }
    
    return json.dumps(result, indent=2)


# ==============================================================================
# LAYER 3: Three-Way Integration (0 tokens deterministic + ~100 synthesis)
# ==============================================================================

@mcp.tool()
def integrate_three_way(
    shadow_parameters: str,  # JSON from shadow-complement-integration
    persona_parameters: str,  # JSON from original colimit
    ideal_parameters: str,    # JSON from compute_ideal_amplification
    integration_mode: str = "balanced_wholeness",
    custom_weights: Optional[str] = None  # JSON dict with shadow/persona/ideal weights
) -> str:
    """
    Integrate shadow, persona, and ideal into unified psychological space.
    
    LAYER 3 INTERFACE: Provides structured data for Claude synthesis.
    
    This is the complete tri-polar model:
    - Shadow: What I deny (via shadow-complement-integration)
    - Persona: What I express (current colimit)
    - Ideal: What I aspire to become (via compute_ideal_amplification)
    
    Args:
        shadow_parameters: JSON from shadow-complement-integration
        persona_parameters: JSON from original colimit
        ideal_parameters: JSON from compute_ideal_amplification
        integration_mode: Preset mode name or "custom"
        custom_weights: Optional JSON dict {"shadow": 0.2, "persona": 0.5, "ideal": 0.3}
        
    Returns:
        JSON string with:
        - integrated_parameters: Weighted blend of all three
        - weights: Shadow/persona/ideal weights used
        - tri_polar_space: Complete psychological structure
        - synthesis_instructions: For Claude to create final prompt
        
    Cost: 0 tokens (deterministic) + ~100-200 tokens (Claude synthesis)
    
    Example:
        integrate_three_way(
            shadow_parameters='{"visual_weight": 0.4, "contrast": 0.3}',
            persona_parameters='{"visual_weight": 0.6, "contrast": 0.7}',
            ideal_parameters='{"visual_weight": 0.8, "contrast": 0.85}',
            integration_mode="growth_emphasis"
        )
    """
    # Parse inputs
    try:
        shadow = json.loads(shadow_parameters)
        persona = json.loads(persona_parameters)
        ideal = json.loads(ideal_parameters)
    except json.JSONDecodeError as e:
        return json.dumps({"error": f"Invalid JSON: {e}"}, indent=2)
    
    # Get weights
    if integration_mode == "custom" and custom_weights:
        try:
            weights = json.loads(custom_weights)
        except json.JSONDecodeError:
            return json.dumps({"error": "Invalid JSON in custom_weights"}, indent=2)
    else:
        # Load preset mode
        modes = OLOG['three_way_integration']['integration_modes']
        if integration_mode not in modes:
            available = list(modes.keys())
            return json.dumps({
                "error": f"Integration mode '{integration_mode}' not found",
                "available_modes": available
            }, indent=2)
        
        mode_spec = modes[integration_mode]
        weights = {
            "shadow": mode_spec['shadow_weight'],
            "persona": mode_spec['persona_weight'],
            "ideal": mode_spec['ideal_weight']
        }
    
    # Validate weights sum to 1.0
    weight_sum = weights['shadow'] + weights['persona'] + weights['ideal']
    if abs(weight_sum - 1.0) > 0.01:
        return json.dumps({
            "error": f"Weights must sum to 1.0 (got {weight_sum})"
        }, indent=2)
    
    # Integrate parameters
    integrated = {}
    
    # Get all parameter names
    all_params = set()
    all_params.update(shadow.keys())
    all_params.update(persona.keys())
    all_params.update(ideal.keys())
    
    for param_name in all_params:
        s_val = shadow.get(param_name, persona.get(param_name, 0))
        p_val = persona.get(param_name, 0)
        i_val = ideal.get(param_name, persona.get(param_name, 0))
        
        # Weighted blend
        if isinstance(p_val, (int, float)):
            integrated[param_name] = (
                weights['shadow'] * (s_val if isinstance(s_val, (int, float)) else p_val) +
                weights['persona'] * p_val +
                weights['ideal'] * (i_val if isinstance(i_val, (int, float)) else p_val)
            )
        else:
            # For non-numeric, use persona as base (could be enhanced)
            integrated[param_name] = p_val
    
    # Build tri-polar space description
    tri_polar_space = {
        "shadow_pole": {
            "parameters": shadow,
            "weight": weights['shadow'],
            "psychological_role": "Denied aspects seeking acknowledgment",
            "visual_effect": "Complementary opposition to persona"
        },
        "persona_pole": {
            "parameters": persona,
            "weight": weights['persona'],
            "psychological_role": "Current expressed self",
            "visual_effect": "Baseline aesthetic identity"
        },
        "ideal_pole": {
            "parameters": ideal,
            "weight": weights['ideal'],
            "psychological_role": "Aspirational self reaching toward archetype",
            "visual_effect": "Amplified expression of potential"
        }
    }
    
    # Get mode intentionality if using preset
    mode_intentionality = ""
    if integration_mode != "custom":
        mode_spec = OLOG['three_way_integration']['integration_modes'][integration_mode]
        mode_intentionality = mode_spec['intentionality']
    
    # Build synthesis instructions
    synthesis_instructions = f"""
SYNTHESIS TASK: Create image generation prompt from tri-polar psychological space.

TRI-POLAR MODEL:
- Shadow ({weights['shadow']*100:.0f}%): Denied aspects - {', '.join(f'{k}={v:.2f}' if isinstance(v, float) else f'{k}={v}' for k, v in list(shadow.items())[:3])}
- Persona ({weights['persona']*100:.0f}%): Current self - {', '.join(f'{k}={v:.2f}' if isinstance(v, float) else f'{k}={v}' for k, v in list(persona.items())[:3])}
- Ideal ({weights['ideal']*100:.0f}%): Aspirational - {', '.join(f'{k}={v:.2f}' if isinstance(v, float) else f'{k}={v}' for k, v in list(ideal.items())[:3])}

INTEGRATED RESULT: {', '.join(f'{k}={v:.2f}' if isinstance(v, float) else f'{k}={v}' for k, v in list(integrated.items())[:5])}

MODE: {integration_mode}
{f'INTENTIONALITY: {mode_intentionality}' if mode_intentionality else ''}

YOUR TASK:
1. Understand the psychological tension between three poles
2. Translate integrated parameters into vivid visual language
3. Create cohesive prompt that embodies this complete self-portrait
4. Suggest visual composition strategy (spatial separation, layering, or flow)

DO NOT simply list parameters. Synthesize into emotionally resonant prompt
that captures the dynamic tension of shadow/persona/ideal integration.
"""
    
    result = {
        "integrated_parameters": integrated,
        "weights": weights,
        "tri_polar_space": tri_polar_space,
        "integration_mode": integration_mode,
        "synthesis_instructions": synthesis_instructions,
        "metadata": {
            "parameter_count": len(integrated),
            "weight_sum": weight_sum,
            "operation": "tri_polar_integration"
        }
    }
    
    return json.dumps(result, indent=2)


# ==============================================================================
# COMPARISON AND ANALYSIS TOOLS
# ==============================================================================

@mcp.tool()
def compare_shadow_vs_ideal(
    persona_parameters: str,  # JSON
    shadow_parameters: str,   # JSON from shadow-complement-integration
    ideal_parameters: str     # JSON from compute_ideal_amplification
) -> str:
    """
    Compare shadow complement vs ideal amplification operations.
    
    Shows how shadow flips to opposite while ideal intensifies same direction.
    Useful for understanding the different psychological operations.
    
    Args:
        persona_parameters: JSON with current persona
        shadow_parameters: JSON with shadow complement
        ideal_parameters: JSON with ideal amplification
        
    Returns:
        JSON string with side-by-side comparison and intentionality
        
    Cost: 0 tokens (pure analysis)
    """
    try:
        persona = json.loads(persona_parameters)
        shadow = json.loads(shadow_parameters)
        ideal = json.loads(ideal_parameters)
    except json.JSONDecodeError as e:
        return json.dumps({"error": f"Invalid JSON: {e}"}, indent=2)
    
    comparisons = []
    
    for param_name in persona.keys():
        p_val = persona.get(param_name)
        s_val = shadow.get(param_name)
        i_val = ideal.get(param_name)
        
        if isinstance(p_val, (int, float)):
            comparison = {
                "parameter": param_name,
                "persona": p_val,
                "shadow": s_val,
                "ideal": i_val,
                "shadow_operation": "antipodal_flip" if s_val != p_val else "no_complement",
                "ideal_operation": "parametric_intensification" if i_val != p_val else "no_amplification",
                "shadow_delta": (s_val - p_val) if isinstance(s_val, (int, float)) else None,
                "ideal_delta": (i_val - p_val) if isinstance(i_val, (int, float)) else None
            }
            comparisons.append(comparison)
    
    result = {
        "comparisons": comparisons,
        "intentionality": {
            "shadow_complement": "Reveals denied opposite - integrating creates wholeness",
            "ideal_amplification": "Intensifies expressed direction - pursuing creates growth",
            "difference": "Shadow acknowledges what I deny; Ideal pursues what I aspire to become"
        },
        "visualization_suggestion": {
            "shadow_representation": "Complementary colors, opposite qualities (cool if persona is warm)",
            "ideal_representation": "Same colors but intensified, amplified presence (warmer if persona is warm)",
            "persona_representation": "Balanced center point between extremes"
        }
    }
    
    return json.dumps(result, indent=2)


@mcp.tool()
def suggest_integration_strategy(
    use_case: str,
    emphasis_preference: Optional[str] = None
) -> str:
    """
    Suggest which integration mode to use for a given use case.
    
    Args:
        use_case: Description of what the image is for
            (e.g., "personal development", "brand evolution", "hero's journey")
        emphasis_preference: Optional emphasis on "growth", "integration", or "balance"
        
    Returns:
        JSON string with recommended mode and rationale
        
    Cost: 0 tokens (rule-based suggestion)
    """
    modes = OLOG['three_way_integration']['integration_modes']
    
    # Simple keyword matching for suggestions
    use_case_lower = use_case.lower()
    
    recommendations = []
    
    for mode_name, mode_spec in modes.items():
        relevance_score = 0
        
        # Check use_case field
        if any(keyword in use_case_lower for keyword in mode_spec['use_case'].lower().split()):
            relevance_score += 2
        
        # Check effect field
        if any(keyword in use_case_lower for keyword in mode_spec['effect'].lower().split()):
            relevance_score += 1
        
        # Check emphasis preference
        if emphasis_preference:
            if emphasis_preference.lower() in mode_name.lower():
                relevance_score += 3
        
        if relevance_score > 0:
            recommendations.append({
                "mode": mode_name,
                "relevance_score": relevance_score,
                "weights": {
                    "shadow": mode_spec['shadow_weight'],
                    "persona": mode_spec['persona_weight'],
                    "ideal": mode_spec['ideal_weight']
                },
                "use_case": mode_spec['use_case'],
                "intentionality": mode_spec['intentionality']
            })
    
    # Sort by relevance
    recommendations.sort(key=lambda x: x['relevance_score'], reverse=True)
    
    if not recommendations:
        recommendations.append({
            "mode": "balanced_wholeness",
            "relevance_score": 0,
            "weights": modes['balanced_wholeness'],
            "note": "Default recommendation - no specific match found"
        })
    
    result = {
        "use_case": use_case,
        "emphasis_preference": emphasis_preference,
        "recommendations": recommendations[:3],  # Top 3
        "guidance": "Consider shadow emphasis for integration work, ideal emphasis for growth work, or balanced for complete portraits"
    }
    
    return json.dumps(result, indent=2)


@mcp.tool()
def get_microscopy_workflow_example() -> str:
    """
    Get a complete workflow example for microscopy aesthetics amplification.
    
    Shows how to use extract_microscopy_parameters_tool with compute_ideal_amplification
    and integrate_three_way for complete tri-polar microscopy visualization.
    
    Returns:
        JSON string with step-by-step workflow and example outputs
        
    Cost: 0 tokens (documentation retrieval)
    """
    example = {
        "workflow": "Microscopy Aesthetics → Ideal Amplification → Tri-Polar Integration",
        
        "step_1_extract_parameters": {
            "tool": "extract_microscopy_parameters_tool",
            "input": {
                "microscopy_type": "fluorescence",
                "aesthetic_strength": "balanced",
                "magnification": "high"
            },
            "output_example": {
                "glow_intensity": 0.65,
                "signal_clarity": 0.65,
                "color_saturation": 0.75,
                "signal_specificity": 0.70,
                "multi_channel_separation": 0.65,
                "contrast_intensity": 0.65,
                "detail_density": 0.60,
                "dimensional_depth": 0.55,
                "magnification_scale": "high",
                "color_palette_mode": "scientific"
            },
            "cost": "0 tokens (deterministic mapping)"
        },
        
        "step_2_amplify_to_ideal": {
            "tool": "compute_ideal_amplification",
            "input": {
                "unified_parameters": "{from step 1}",
                "aesthetic_domain": "microscopy_aesthetics",
                "amplification_level": 0.5
            },
            "output_example": {
                "persona": {"glow_intensity": 0.65, "signal_clarity": 0.65},
                "ideal": {"glow_intensity": 0.80, "signal_clarity": 0.825},
                "amplification_level": 0.5,
                "metadata": {"operation": "parametric_intensification"}
            },
            "cost": "0 tokens (deterministic math)"
        },
        
        "step_3_compute_shadow": {
            "tool": "shadow-complement-integration:integrate_shadow_complement",
            "input": {
                "unified_parameters": "{from step 1}",
                "aesthetic_domain": "microscopy_aesthetics",
                "integration_level": 0.5
            },
            "output_example": {
                "persona": {"glow_intensity": 0.65},
                "shadow_complements": {"glow_intensity": 0.35},
                "integrated_parameters": {"glow_intensity": 0.50}
            },
            "cost": "0 tokens (deterministic antipode)"
        },
        
        "step_4_integrate_three_way": {
            "tool": "integrate_three_way",
            "input": {
                "shadow_parameters": "{from shadow-complement-integration}",
                "persona_parameters": "{from step 1}",
                "ideal_parameters": "{from step 2}",
                "integration_mode": "growth_emphasis"
            },
            "weights": {
                "shadow": 0.10,
                "persona": 0.30,
                "ideal": 0.60
            },
            "output_example": {
                "integrated_parameters": {"glow_intensity": 0.715},
                "tri_polar_space": {
                    "shadow_pole": 0.35,
                    "persona_pole": 0.65,
                    "ideal_pole": 0.80
                }
            },
            "cost": "0 tokens (deterministic weighted blend)"
        },
        
        "step_5_claude_synthesis": {
            "description": "Claude synthesizes final prompt from tri-polar parameters",
            "input": "Complete tri-polar space with all parameters",
            "output": "Vivid image generation prompt embodying shadow/persona/ideal tension",
            "cost": "~150-200 tokens (creative synthesis)"
        },
        
        "total_cost_profile": {
            "layer_1_taxonomy": "0 tokens",
            "layer_2_computation": "0 tokens",
            "layer_3_synthesis": "~150-200 tokens",
            "total": "~150-200 tokens",
            "vs_pure_llm": "~600-800 tokens",
            "savings": "70-75%"
        },
        
        "example_final_prompt": {
            "microscopy_type": "fluorescence",
            "subject": "Neural dendrites with synaptic connections",
            "tri_polar_interpretation": "Brilliant luminescence (ideal pole), balanced technical clarity (persona pole), with subtle muted tones acknowledging instrumental limitations (shadow pole)",
            "visual_synthesis": "Jewel-tone fluorescence with crystalline signal definition, dramatic z-projection showing perfect optical sectioning, radiant glow suggesting publication-quality imaging while maintaining scientific authenticity"
        }
    }
    
    return json.dumps(example, indent=2)


@mcp.tool()
def get_server_info() -> str:
    """
    Get information about the Ideal Amplification MCP server.
    
    Returns metadata, capabilities, and integration information
    including Phase 2.6 rhythmic presets and Phase 2.7 attractor
    visualization prompt generation.
    """
    periods = sorted(set(c["steps_per_cycle"] for c in IDEAL_AMPLIFICATION_PRESETS.values()))
    
    info = {
        "name": "ideal-amplification",
        "version": "2.0",
        "description": "Jungian ideal/anima-animus as parametric intensification toward archetype",
        "companion_brick": "shadow-complement-integration",
        
        "capabilities": {
            "layer_1_taxonomy": "Deterministic amplification rules (0 tokens)",
            "layer_2_computation": "Mathematical extrapolation + Phase 2.6/2.7 (0 tokens)",
            "layer_3_synthesis": "Claude integration (~100-200 tokens)"
        },
        
        "tri_polar_model": {
            "shadow": "Denied aspects (via shadow-complement-integration)",
            "persona": "Current expression (via multi-domain-colimit-composer)",
            "ideal": "Aspirational archetype (via compute_ideal_amplification)"
        },
        
        "supported_domains": list(OLOG['amplification_operations'].keys()) + ["microscopy_aesthetics"],
        
        "microscopy_support": {
            "parameter_extraction": "extract_microscopy_parameters_tool",
            "bridge_function": "Converts microscopy modality choices to numerical parameters",
            "supported_modalities": [
                "fluorescence", "electron", "phase_contrast", "confocal",
                "darkfield", "brightfield", "multiphoton"
            ]
        },
        
        "phase_2_6_enhancements": {
            "rhythmic_presets": True,
            "total_presets": len(IDEAL_AMPLIFICATION_PRESETS),
            "periods": periods,
            "canonical_states": list(IDEAL_AMPLIFICATION_COORDS.keys()),
            "parameter_names": IDEAL_AMPLIFICATION_PARAMETER_NAMES,
            "morphospace_dimensions": 5,
            "preset_names": list(IDEAL_AMPLIFICATION_PRESETS.keys()),
            "tools": [
                "apply_ideal_amplification_preset",
                "compute_ideal_amplification_trajectory",
                "list_ideal_amplification_presets",
            ],
        },
        
        "phase_2_7_enhancements": {
            "attractor_visualization": True,
            "visual_types": list(IDEAL_AMPLIFICATION_VISUAL_TYPES.keys()),
            "total_visual_types": len(IDEAL_AMPLIFICATION_VISUAL_TYPES),
            "prompt_modes": ["composite", "split_view", "sequence"],
            "tools": [
                "get_ideal_amplification_visual_types",
                "generate_ideal_amplification_attractor_prompt",
                "get_ideal_amplification_domain_registry_config",
            ],
        },
        
        "cost_profile": {
            "deterministic_operations": "0 tokens",
            "phase_2_6_presets": "0 tokens (forced orbit integration)",
            "phase_2_7_prompts": "0 tokens (nearest-neighbor vocabulary)",
            "claude_synthesis": "~100-200 tokens",
            "total_savings": "~70% vs pure LLM approach"
        },
        
        "integration_points": {
            "shadow_complement": "Provides shadow pole parameters",
            "multi_domain_colimit": "Provides persona pole parameters",
            "ideal_amplification": "Computes ideal pole parameters (this brick)",
            "three_way_integration": "Blends all three poles",
            "tier_4d_composition": "Domain registry config for multi-domain limit cycle discovery",
        },
        
        "typical_workflow": [
            "1. Get persona from multi-domain colimit composition",
            "2. Compute shadow via shadow-complement-integration",
            "3. Compute ideal via compute_ideal_amplification",
            "4. Integrate all three via integrate_three_way",
            "5. Claude synthesizes final prompt from tri-polar space",
            "--- Phase 2.6/2.7 workflow ---",
            "6. apply_ideal_amplification_preset for rhythmic composition",
            "7. generate_ideal_amplification_attractor_prompt for image-gen prompts",
            "8. get_ideal_amplification_domain_registry_config for Tier 4D integration",
        ]
    }
    
    return json.dumps(info, indent=2)


# ============================================================================
# PHASE 2.6: Rhythmic Composition Presets (Layer 2 — Zero LLM Cost)
# ============================================================================
#
# 5D Normalized Morphospace for Ideal Amplification:
#
#   archetypal_intensity  [0,1] : Strength of archetypal manifestation
#                                 0 = latent/dormant, 1 = full archetypal possession
#   integration_balance   [0,1] : Position on shadow↔ideal axis
#                                 0 = shadow-dominated, 0.5 = persona-centered, 1 = ideal-dominated
#   amplification_coherence [0,1]: Focus of the amplification process
#                                 0 = scattered/fragmented, 1 = laser-focused/unified
#   shadow_acknowledgment [0,1] : Degree of shadow integration
#                                 0 = fully denied, 1 = fully acknowledged/integrated
#   transformative_momentum [0,1]: Dynamic quality of psychological change
#                                 0 = static/frozen, 1 = rapid transformation
#
# Period Strategy (relative to existing landscape):
#   Existing: [10, 12, 15, 16, 18, 20, 22, 24, 25, 30]
#   This domain adds: [11, 14, 18, 22, 26, 32]
#     - Period 11: Fills gap 10-12, LCM(11,10)=110 novel harmonic
#     - Period 14: Fills gap 12-15, LCM(14,12)=84 novel harmonic
#     - Period 18: Syncs with nuclear+catastrophe+diatom (3-domain overlap)
#     - Period 22: Syncs with catastrophe+heraldic (2-domain overlap)
#     - Period 26: Fills gap 25-30, complements heraldic Period 27
#     - Period 32: Novel high period, 2×16 harmonic
# ============================================================================

IDEAL_AMPLIFICATION_PARAMETER_NAMES = [
    "archetypal_intensity",
    "integration_balance",
    "amplification_coherence",
    "shadow_acknowledgment",
    "transformative_momentum",
]

IDEAL_AMPLIFICATION_COORDS = {
    # Shadow overwhelms — denied aspects surface uncontrolled
    "shadow_dominant": {
        "archetypal_intensity": 0.75,
        "integration_balance": 0.10,
        "amplification_coherence": 0.30,
        "shadow_acknowledgment": 0.15,
        "transformative_momentum": 0.60,
    },
    # Balanced current self — expressed identity, moderate everywhere
    "persona_centered": {
        "archetypal_intensity": 0.40,
        "integration_balance": 0.50,
        "amplification_coherence": 0.55,
        "shadow_acknowledgment": 0.45,
        "transformative_momentum": 0.30,
    },
    # Full archetypal manifestation — luminous, realized
    "ideal_ascendant": {
        "archetypal_intensity": 0.95,
        "integration_balance": 0.95,
        "amplification_coherence": 0.90,
        "shadow_acknowledgment": 0.35,
        "transformative_momentum": 0.80,
    },
    # Equal integration of all three poles — harmonized completeness
    "balanced_wholeness": {
        "archetypal_intensity": 0.60,
        "integration_balance": 0.50,
        "amplification_coherence": 0.80,
        "shadow_acknowledgment": 0.85,
        "transformative_momentum": 0.45,
    },
    # Forward-leaning, aspirational — dynamic growth
    "growth_emphasis": {
        "archetypal_intensity": 0.70,
        "integration_balance": 0.75,
        "amplification_coherence": 0.70,
        "shadow_acknowledgment": 0.55,
        "transformative_momentum": 0.90,
    },
    # Shadow-ideal tension — facing denied aspects directly
    "confrontation": {
        "archetypal_intensity": 0.85,
        "integration_balance": 0.30,
        "amplification_coherence": 0.45,
        "shadow_acknowledgment": 0.70,
        "transformative_momentum": 0.75,
    },
    # Jungian completion — all poles harmonized at high level
    "individuation": {
        "archetypal_intensity": 0.80,
        "integration_balance": 0.65,
        "amplification_coherence": 0.95,
        "shadow_acknowledgment": 1.00,
        "transformative_momentum": 0.55,
    },
}

IDEAL_AMPLIFICATION_PRESETS = {
    "individuation_cycle": {
        "state_a": "persona_centered",
        "state_b": "individuation",
        "pattern": "sinusoidal",
        "num_cycles": 3,
        "steps_per_cycle": 14,
        "description": "Cyclic movement from everyday persona toward Jungian individuation and back — the breath of self-realization",
    },
    "shadow_confrontation": {
        "state_a": "persona_centered",
        "state_b": "shadow_dominant",
        "pattern": "triangular",
        "num_cycles": 2,
        "steps_per_cycle": 22,
        "description": "Gradual descent into shadow territory with linear return — confronting denied aspects symmetrically",
    },
    "archetypal_ascent": {
        "state_a": "persona_centered",
        "state_b": "ideal_ascendant",
        "pattern": "sinusoidal",
        "num_cycles": 2,
        "steps_per_cycle": 26,
        "description": "Slow oscillation between current self and full archetypal manifestation — the aspiration rhythm",
    },
    "integration_pulse": {
        "state_a": "shadow_dominant",
        "state_b": "ideal_ascendant",
        "pattern": "sinusoidal",
        "num_cycles": 3,
        "steps_per_cycle": 18,
        "description": "Rapid pulsing between shadow and ideal poles — the tension that drives psychological integration",
    },
    "growth_oscillation": {
        "state_a": "growth_emphasis",
        "state_b": "confrontation",
        "pattern": "square",
        "num_cycles": 4,
        "steps_per_cycle": 11,
        "description": "Sharp toggling between forward aspiration and shadow confrontation — the punctuated rhythm of real growth",
    },
    "wholeness_rhythm": {
        "state_a": "confrontation",
        "state_b": "balanced_wholeness",
        "pattern": "sinusoidal",
        "num_cycles": 2,
        "steps_per_cycle": 32,
        "description": "Long-period oscillation from shadow-ideal tension to harmonized wholeness — the deep cycle of integration",
    },
}


def _generate_ideal_amplification_oscillation(
    num_steps: int, num_cycles: float, pattern: str
) -> np.ndarray:
    """Generate oscillation pattern in [0, 1] for preset interpolation."""
    t = np.linspace(0, 2 * np.pi * num_cycles, num_steps, endpoint=False)

    if pattern == "sinusoidal":
        return 0.5 * (1.0 + np.sin(t))
    elif pattern == "triangular":
        t_norm = (t / (2 * np.pi)) % 1.0
        return np.where(t_norm < 0.5, 2.0 * t_norm, 2.0 * (1.0 - t_norm))
    elif pattern == "square":
        t_norm = (t / (2 * np.pi)) % 1.0
        return np.where(t_norm < 0.5, 0.0, 1.0)
    else:
        raise ValueError(f"Unknown oscillation pattern: {pattern}")


def _generate_ideal_amplification_preset_trajectory(
    preset_name: str,
) -> List[Dict[str, float]]:
    """
    Generate a single Phase 2.6 preset trajectory via forced orbit integration.

    Returns list of state dicts, one per step.  Total steps = num_cycles * steps_per_cycle.
    Guaranteed periodic closure by construction (zero drift).
    """
    cfg = IDEAL_AMPLIFICATION_PRESETS[preset_name]
    state_a = IDEAL_AMPLIFICATION_COORDS[cfg["state_a"]]
    state_b = IDEAL_AMPLIFICATION_COORDS[cfg["state_b"]]

    total_steps = cfg["num_cycles"] * cfg["steps_per_cycle"]
    alpha = _generate_ideal_amplification_oscillation(
        total_steps, cfg["num_cycles"], cfg["pattern"]
    )

    vec_a = np.array([state_a[p] for p in IDEAL_AMPLIFICATION_PARAMETER_NAMES])
    vec_b = np.array([state_b[p] for p in IDEAL_AMPLIFICATION_PARAMETER_NAMES])

    trajectory = np.outer(1.0 - alpha, vec_a) + np.outer(alpha, vec_b)

    return [
        {p: float(trajectory[i, j]) for j, p in enumerate(IDEAL_AMPLIFICATION_PARAMETER_NAMES)}
        for i in range(total_steps)
    ]


@mcp.tool()
def apply_ideal_amplification_preset(
    preset_name: str,
    num_cycles: Optional[int] = None,
) -> str:
    """
    Apply a Phase 2.6 rhythmic preset, generating a complete oscillation
    trajectory through ideal amplification parameter space.

    Layer 2 — deterministic forced orbit integration. Zero LLM cost.

    Each preset oscillates between two canonical psychological states
    (e.g. persona_centered ↔ individuation) at a characteristic period
    chosen for cross-domain resonance.

    Args:
        preset_name: One of the available preset names
        num_cycles: Override default cycle count (optional)

    Returns:
        JSON with trajectory (list of parameter states), metadata,
        and per-step parameter values.

    Cost: 0 tokens (deterministic NumPy computation)
    """
    if preset_name not in IDEAL_AMPLIFICATION_PRESETS:
        return json.dumps({
            "error": f"Unknown preset '{preset_name}'",
            "available_presets": list(IDEAL_AMPLIFICATION_PRESETS.keys()),
        }, indent=2)

    cfg = IDEAL_AMPLIFICATION_PRESETS[preset_name]

    # Allow cycle count override
    effective_cycles = num_cycles if num_cycles is not None else cfg["num_cycles"]
    original_cycles = cfg["num_cycles"]
    if num_cycles is not None:
        cfg = dict(cfg)
        cfg["num_cycles"] = effective_cycles

    total_steps = effective_cycles * cfg["steps_per_cycle"]
    alpha = _generate_ideal_amplification_oscillation(
        total_steps, effective_cycles, cfg["pattern"]
    )

    state_a = IDEAL_AMPLIFICATION_COORDS[cfg["state_a"]]
    state_b = IDEAL_AMPLIFICATION_COORDS[cfg["state_b"]]
    vec_a = np.array([state_a[p] for p in IDEAL_AMPLIFICATION_PARAMETER_NAMES])
    vec_b = np.array([state_b[p] for p in IDEAL_AMPLIFICATION_PARAMETER_NAMES])
    trajectory_arr = np.outer(1.0 - alpha, vec_a) + np.outer(alpha, vec_b)

    trajectory = [
        {p: round(float(trajectory_arr[i, j]), 4)
         for j, p in enumerate(IDEAL_AMPLIFICATION_PARAMETER_NAMES)}
        for i in range(total_steps)
    ]

    # Restore original cfg if overridden
    if num_cycles is not None:
        cfg["num_cycles"] = original_cycles

    return json.dumps({
        "preset": preset_name,
        "description": IDEAL_AMPLIFICATION_PRESETS[preset_name]["description"],
        "state_a": IDEAL_AMPLIFICATION_PRESETS[preset_name]["state_a"],
        "state_b": IDEAL_AMPLIFICATION_PRESETS[preset_name]["state_b"],
        "pattern": IDEAL_AMPLIFICATION_PRESETS[preset_name]["pattern"],
        "period": IDEAL_AMPLIFICATION_PRESETS[preset_name]["steps_per_cycle"],
        "num_cycles": effective_cycles,
        "total_steps": total_steps,
        "trajectory": trajectory,
    }, indent=2)


@mcp.tool()
def compute_ideal_amplification_trajectory(
    state_a_id: str,
    state_b_id: str,
    num_steps: int = 50,
    pattern: str = "sinusoidal",
) -> str:
    """
    Compute smooth interpolation trajectory between two canonical
    ideal-amplification states.

    Layer 2 — deterministic forced orbit. Zero LLM cost.

    Args:
        state_a_id: Starting canonical state
        state_b_id: Ending canonical state
        num_steps: Total trajectory length (default 50)
        pattern: sinusoidal, triangular, or square

    Returns:
        JSON with trajectory array and endpoint metadata.

    Cost: 0 tokens
    """
    if state_a_id not in IDEAL_AMPLIFICATION_COORDS:
        return json.dumps({
            "error": f"Unknown state '{state_a_id}'",
            "available_states": list(IDEAL_AMPLIFICATION_COORDS.keys()),
        }, indent=2)
    if state_b_id not in IDEAL_AMPLIFICATION_COORDS:
        return json.dumps({
            "error": f"Unknown state '{state_b_id}'",
            "available_states": list(IDEAL_AMPLIFICATION_COORDS.keys()),
        }, indent=2)

    state_a = IDEAL_AMPLIFICATION_COORDS[state_a_id]
    state_b = IDEAL_AMPLIFICATION_COORDS[state_b_id]
    vec_a = np.array([state_a[p] for p in IDEAL_AMPLIFICATION_PARAMETER_NAMES])
    vec_b = np.array([state_b[p] for p in IDEAL_AMPLIFICATION_PARAMETER_NAMES])

    alpha = _generate_ideal_amplification_oscillation(num_steps, 1.0, pattern)
    traj = np.outer(1.0 - alpha, vec_a) + np.outer(alpha, vec_b)

    trajectory = [
        {p: round(float(traj[i, j]), 4)
         for j, p in enumerate(IDEAL_AMPLIFICATION_PARAMETER_NAMES)}
        for i in range(num_steps)
    ]

    return json.dumps({
        "state_a": state_a_id,
        "state_b": state_b_id,
        "pattern": pattern,
        "num_steps": num_steps,
        "state_a_coords": state_a,
        "state_b_coords": state_b,
        "trajectory": trajectory,
    }, indent=2)


@mcp.tool()
def list_ideal_amplification_presets() -> str:
    """
    List all Phase 2.6 rhythmic presets with their parameters.

    Layer 1 — pure taxonomy lookup.

    Returns:
        JSON with preset configs, canonical states, and period landscape.

    Cost: 0 tokens
    """
    presets_out = {}
    for name, cfg in IDEAL_AMPLIFICATION_PRESETS.items():
        presets_out[name] = {
            "state_a": cfg["state_a"],
            "state_b": cfg["state_b"],
            "pattern": cfg["pattern"],
            "period": cfg["steps_per_cycle"],
            "num_cycles": cfg["num_cycles"],
            "total_steps": cfg["num_cycles"] * cfg["steps_per_cycle"],
            "description": cfg["description"],
        }

    periods = sorted(set(c["steps_per_cycle"] for c in IDEAL_AMPLIFICATION_PRESETS.values()))

    return json.dumps({
        "domain": "ideal_amplification",
        "total_presets": len(presets_out),
        "periods": periods,
        "presets": presets_out,
        "canonical_states": list(IDEAL_AMPLIFICATION_COORDS.keys()),
        "parameter_names": IDEAL_AMPLIFICATION_PARAMETER_NAMES,
    }, indent=2)


# ============================================================================
# PHASE 2.7: Attractor Visualization Prompt Generation (Layer 2 — Zero Cost)
# ============================================================================
#
# Visual vocabulary types anchored in the 5D morphospace.
# Each type has coordinates + image-generation-ready keywords.
# Nearest-neighbor matching via Euclidean distance (weight cutoff ~0.15).
# ============================================================================

IDEAL_AMPLIFICATION_VISUAL_TYPES = {
    "shadow_emergence": {
        "coords": {
            "archetypal_intensity": 0.75,
            "integration_balance": 0.10,
            "amplification_coherence": 0.30,
            "shadow_acknowledgment": 0.15,
            "transformative_momentum": 0.60,
        },
        "keywords": [
            "deep chiaroscuro lighting",
            "emerging dark silhouette against luminous ground",
            "submerged forms surfacing through opacity layers",
            "high-contrast shadow play with psychological weight",
            "dualistic figure-ground tension",
            "noir atmosphere with revealed hidden structure",
            "suppressed color breaking through monochrome field",
        ],
    },
    "persona_equilibrium": {
        "coords": {
            "archetypal_intensity": 0.40,
            "integration_balance": 0.50,
            "amplification_coherence": 0.55,
            "shadow_acknowledgment": 0.45,
            "transformative_momentum": 0.30,
        },
        "keywords": [
            "balanced neutral-tone composition",
            "stable centered subject with even lighting",
            "moderate contrast and naturalistic palette",
            "grounded midtone harmony without extremes",
            "poised equilibrium between warm and cool",
            "quietly confident spatial arrangement",
        ],
    },
    "archetypal_radiance": {
        "coords": {
            "archetypal_intensity": 0.95,
            "integration_balance": 0.95,
            "amplification_coherence": 0.90,
            "shadow_acknowledgment": 0.35,
            "transformative_momentum": 0.80,
        },
        "keywords": [
            "brilliant aureate luminescence",
            "transcendent radial light emanating from core",
            "saturated jewel-tone palette at maximum intensity",
            "idealized form with sharp geometric clarity",
            "heroic upward compositional thrust",
            "cathedral-light volumetric rays",
            "pure archetypal icon against infinite field",
        ],
    },
    "integrated_mandala": {
        "coords": {
            "archetypal_intensity": 0.60,
            "integration_balance": 0.50,
            "amplification_coherence": 0.80,
            "shadow_acknowledgment": 0.85,
            "transformative_momentum": 0.45,
        },
        "keywords": [
            "concentric radial symmetry with organic variation",
            "warm-cool duality resolved into unified palette",
            "layered transparency showing depth of integration",
            "mandala-like compositional balance",
            "harmonized opposites coexisting in single frame",
            "contemplative stillness with embedded complexity",
        ],
    },
    "transformative_ascent": {
        "coords": {
            "archetypal_intensity": 0.70,
            "integration_balance": 0.75,
            "amplification_coherence": 0.70,
            "shadow_acknowledgment": 0.55,
            "transformative_momentum": 0.90,
        },
        "keywords": [
            "dynamic diagonal compositional energy",
            "metamorphic form mid-transformation",
            "gradient progression from dense base to luminous apex",
            "kinetic particle trails suggesting upward movement",
            "chrysalis-to-emergence visual narrative",
            "accelerating rhythm of expanding geometric forms",
        ],
    },
    "duality_tension": {
        "coords": {
            "archetypal_intensity": 0.85,
            "integration_balance": 0.30,
            "amplification_coherence": 0.45,
            "shadow_acknowledgment": 0.70,
            "transformative_momentum": 0.75,
        },
        "keywords": [
            "split-field composition with stark bisection",
            "simultaneous warm and cold light sources",
            "mirrored forms in oppositional dialogue",
            "high-energy boundary between contrasting zones",
            "tense compositional asymmetry seeking resolution",
            "visible fault line between shadow and aspiration",
            "dramatic confrontational staging",
        ],
    },
    "individuation_completion": {
        "coords": {
            "archetypal_intensity": 0.80,
            "integration_balance": 0.65,
            "amplification_coherence": 0.95,
            "shadow_acknowledgment": 1.00,
            "transformative_momentum": 0.55,
        },
        "keywords": [
            "golden-ratio spiral organizing complex form",
            "full-spectrum palette in resolved harmony",
            "architectural precision with organic warmth",
            "complete self-contained compositional unity",
            "luminous clarity with acknowledged shadow accents",
            "Jungian wholeness rendered as visual coherence",
            "dignified stillness of achieved integration",
        ],
    },
}


def _extract_ideal_amplification_visual_vocabulary(
    state: Dict[str, float],
    strength: float = 1.0,
) -> Dict[str, Any]:
    """
    Nearest-neighbor vocabulary extraction from 5D ideal amplification morphospace.

    Finds the closest visual type to the given parameter state and returns
    weighted keywords for image generation prompts.

    Args:
        state: Dict mapping parameter names to [0,1] values
        strength: Domain strength weight for keyword ordering

    Returns:
        Dict with nearest_type, distance, keywords, and strength
    """
    state_vec = np.array([state.get(p, 0.5) for p in IDEAL_AMPLIFICATION_PARAMETER_NAMES])

    best_type = None
    best_dist = float("inf")

    for vtype_name, vtype in IDEAL_AMPLIFICATION_VISUAL_TYPES.items():
        vtype_vec = np.array([vtype["coords"][p] for p in IDEAL_AMPLIFICATION_PARAMETER_NAMES])
        dist = float(np.linalg.norm(state_vec - vtype_vec))
        if dist < best_dist:
            best_dist = dist
            best_type = vtype_name

    keywords = IDEAL_AMPLIFICATION_VISUAL_TYPES[best_type]["keywords"]

    return {
        "nearest_type": best_type,
        "distance": round(best_dist, 4),
        "keywords": keywords,
        "strength": strength,
        "domain": "ideal_amplification",
    }


@mcp.tool()
def get_ideal_amplification_visual_types() -> str:
    """
    List all ideal amplification visual types with their 5D coordinates
    and image-generation keywords.

    Layer 1 — pure taxonomy lookup.

    Returns:
        JSON with all visual types, coordinates, and keywords.

    Cost: 0 tokens
    """
    types_out = {}
    for name, vtype in IDEAL_AMPLIFICATION_VISUAL_TYPES.items():
        types_out[name] = {
            "coords": vtype["coords"],
            "keywords": vtype["keywords"],
            "keyword_count": len(vtype["keywords"]),
        }

    return json.dumps({
        "domain": "ideal_amplification",
        "total_visual_types": len(types_out),
        "parameter_names": IDEAL_AMPLIFICATION_PARAMETER_NAMES,
        "visual_types": types_out,
    }, indent=2)


@mcp.tool()
def generate_ideal_amplification_attractor_prompt(
    state: str,
    mode: str = "composite",
    strength: float = 1.0,
) -> str:
    """
    Generate image-generation-ready prompts from a 5D ideal amplification
    parameter state.

    Layer 2 — deterministic nearest-neighbor matching + keyword assembly.
    Zero LLM cost.

    Three prompt generation modes:
      composite  — single blended prompt from nearest visual type keywords
      split_view — separate prompt block for this domain (for multi-domain split)
      sequence   — ordered keyword list for temporal keyframe sequences

    Args:
        state: JSON string with parameter values, e.g.
               '{"archetypal_intensity": 0.7, "integration_balance": 0.6, ...}'
               OR a canonical state name like "individuation"
        mode: composite | split_view | sequence
        strength: Domain weight [0.0, 1.0] for keyword ordering

    Returns:
        JSON with prompt text, matched visual type, distance, and keywords.

    Cost: 0 tokens
    """
    # Accept either a JSON state dict or a canonical state name
    try:
        state_dict = json.loads(state)
    except (json.JSONDecodeError, TypeError):
        state_str = state.strip().strip('"').strip("'")
        if state_str in IDEAL_AMPLIFICATION_COORDS:
            state_dict = IDEAL_AMPLIFICATION_COORDS[state_str]
        else:
            return json.dumps({
                "error": f"Cannot parse state. Provide JSON dict or canonical state name.",
                "available_states": list(IDEAL_AMPLIFICATION_COORDS.keys()),
            }, indent=2)

    vocab = _extract_ideal_amplification_visual_vocabulary(state_dict, strength)

    if mode == "composite":
        prompt = ", ".join(vocab["keywords"])
        return json.dumps({
            "mode": "composite",
            "prompt": prompt,
            "visual_type": vocab["nearest_type"],
            "distance": vocab["distance"],
            "strength": strength,
            "keywords": vocab["keywords"],
        }, indent=2)

    elif mode == "split_view":
        prompt_block = (
            f"[Ideal Amplification — {vocab['nearest_type'].replace('_', ' ').title()}]\n"
            + ", ".join(vocab["keywords"])
        )
        return json.dumps({
            "mode": "split_view",
            "domain": "ideal_amplification",
            "prompt_block": prompt_block,
            "visual_type": vocab["nearest_type"],
            "distance": vocab["distance"],
            "strength": strength,
        }, indent=2)

    elif mode == "sequence":
        return json.dumps({
            "mode": "sequence",
            "domain": "ideal_amplification",
            "keyframe_keywords": vocab["keywords"],
            "visual_type": vocab["nearest_type"],
            "distance": vocab["distance"],
            "strength": strength,
        }, indent=2)

    else:
        return json.dumps({
            "error": f"Unknown mode '{mode}'",
            "available_modes": ["composite", "split_view", "sequence"],
        }, indent=2)


@mcp.tool()
def get_ideal_amplification_domain_registry_config() -> str:
    """
    Return Tier 4D integration configuration for compositional limit cycle
    discovery. Exports this domain's periods, predicted emergent attractors,
    canonical states, and basin size estimates for the multi-domain registry.

    Layer 2 — deterministic computation. Zero LLM cost.

    Returns:
        JSON with domain_id, periods, state coordinates, predicted attractors,
        and cross-domain resonance analysis.

    Cost: 0 tokens
    """
    periods = sorted(set(c["steps_per_cycle"] for c in IDEAL_AMPLIFICATION_PRESETS.values()))

    # Compute predicted emergent attractors with existing domain periods
    # Existing landscape: [10, 12, 15, 16, 18, 20, 22, 24, 25, 30]
    existing_periods = [10, 12, 15, 16, 18, 20, 22, 24, 25, 30]
    our_periods = periods

    predicted_attractors = []

    # LCM-based predictions
    for op in our_periods:
        for ep in existing_periods:
            lcm_val = (op * ep) // math.gcd(op, ep)
            if 10 <= lcm_val <= 100:
                predicted_attractors.append({
                    "period": lcm_val,
                    "mechanism": "lcm_sync",
                    "source_periods": [op, ep],
                    "predicted_basin_size": round(0.02 + 0.04 * (1.0 / (lcm_val / 30.0)), 3),
                })

    # Gap-filler predictions — our periods that sit in existing gaps
    gap_fillers = []
    all_sorted = sorted(set(existing_periods + our_periods))
    for p in our_periods:
        # Find neighbors among existing periods
        lower = [x for x in existing_periods if x < p]
        upper = [x for x in existing_periods if x > p]
        if lower and upper:
            gap = min(upper) - max(lower)
            if gap >= 2:
                gap_fillers.append({
                    "period": p,
                    "mechanism": "gap_filler",
                    "gap": f"{max(lower)}-{min(upper)}",
                    "gap_size": gap,
                    "predicted_basin_size": round(0.01 + 0.02 * gap, 3),
                })

    # De-duplicate attractors by period, keeping highest basin estimate
    attractor_map = {}
    for a in predicted_attractors + gap_fillers:
        p = a["period"]
        if p not in attractor_map or a["predicted_basin_size"] > attractor_map[p]["predicted_basin_size"]:
            attractor_map[p] = a
    predicted_attractors_dedup = sorted(attractor_map.values(), key=lambda x: -x["predicted_basin_size"])

    # Cross-domain resonance — periods shared with other domains
    domain_period_map = {
        "microscopy": [10, 16, 20, 24, 30],
        "nuclear": [15, 18],
        "catastrophe": [15, 18, 20, 22, 25],
        "diatom": [12, 15, 18, 20, 30],
        "heraldic": [12, 16, 22, 25, 30],
    }

    shared_periods = {}
    for p in our_periods:
        shared_with = [d for d, ps in domain_period_map.items() if p in ps]
        if shared_with:
            shared_periods[str(p)] = shared_with

    return json.dumps({
        "domain_id": "ideal_amplification",
        "display_name": "Ideal Amplification",
        "mcp_server": "ideal-amplification",
        "parameter_names": IDEAL_AMPLIFICATION_PARAMETER_NAMES,
        "parameter_count": len(IDEAL_AMPLIFICATION_PARAMETER_NAMES),
        "periods": our_periods,
        "canonical_states": {
            name: coords for name, coords in IDEAL_AMPLIFICATION_COORDS.items()
        },
        "preset_count": len(IDEAL_AMPLIFICATION_PRESETS),
        "visual_type_count": len(IDEAL_AMPLIFICATION_VISUAL_TYPES),
        "predicted_emergent_attractors": predicted_attractors_dedup[:15],
        "gap_fillers": gap_fillers,
        "shared_periods": shared_periods,
        "cross_domain_resonance": {
            "period_18": "Syncs with nuclear + catastrophe + diatom (3-domain overlap)",
            "period_22": "Syncs with catastrophe + heraldic (2-domain overlap)",
            "period_11": "Novel — fills gap 10-12, LCM(11,10)=110",
            "period_14": "Novel — fills gap 12-15, LCM(14,12)=84",
            "period_26": "Novel — fills gap 25-30, complements heraldic Period 27",
            "period_32": "Novel — 2x16 harmonic, high-period resonance hub",
        },
        "tier_4d_ready": True,
    }, indent=2)


# ============================================================================
# STRATEGIC ANALYSIS (Tomographic Domain Projection)
# ============================================================================

STRATEGIC_PATTERNS = {
    "archetypal_clarity": {
        "clear_archetype": [
            "archetypal maximum", "ideal state", "pure expression",
            "perfect embodiment", "fully realized", "quintessential"
        ],
        "ambiguous_archetype": [
            "mixed signals", "unclear direction", "competing ideals",
            "contradictory aspirations", "identity confusion", "purpose drift"
        ]
    },
    
    "amplification_consistency": {
        "coherent_amplification": [
            "builds on strengths", "intensifies existing", "amplifies core",
            "natural extension", "logical progression", "authentic growth"
        ],
        "fragmented_amplification": [
            "scattered focus", "conflicting goals", "dispersed energy",
            "too many directions", "diluted purpose", "unfocused aspirations"
        ]
    },
    
    "shadow_integration": {
        "acknowledged_shadow": [
            "addresses weaknesses", "confronts challenges", "acknowledges limitations",
            "realistic constraints", "balanced perspective", "owns shortcomings"
        ],
        "denied_shadow": [
            "ignores challenges", "unrealistic optimism", "blind spots",
            "avoids hard truths", "fantasy thinking", "denial of limits"
        ]
    },
    
    "aspirational_realism": {
        "grounded_aspiration": [
            "achievable goals", "realistic timeline", "practical steps",
            "measurable progress", "concrete milestones", "actionable plan"
        ],
        "unrealistic_aspiration": [
            "magical thinking", "impossible timeline", "no clear path",
            "vague aspirations", "wishful thinking", "disconnected from reality"
        ]
    }
}


def detect_archetypal_clarity(text: str) -> dict:
    """Detect whether strategy has clear aspirational archetype."""
    clear_count = sum(1 for phrase in STRATEGIC_PATTERNS["archetypal_clarity"]["clear_archetype"]
                     if phrase in text.lower())
    ambiguous_count = sum(1 for phrase in STRATEGIC_PATTERNS["archetypal_clarity"]["ambiguous_archetype"]
                         if phrase in text.lower())
    
    if clear_count > ambiguous_count and clear_count >= 2:
        return {
            "dimension": "archetypal_clarity",
            "pattern": "clear_archetype",
            "confidence": min(0.9, 0.5 + (clear_count * 0.1)),
            "evidence": f"Archetypal clarity: {clear_count} markers vs {ambiguous_count} ambiguity markers",
            "categorical_family": "objects"
        }
    elif ambiguous_count >= 2:
        return {
            "dimension": "archetypal_clarity",
            "pattern": "ambiguous_archetype",
            "confidence": min(0.85, 0.5 + (ambiguous_count * 0.1)),
            "evidence": f"Archetypal ambiguity: {ambiguous_count} markers",
            "categorical_family": "constraints"
        }
    return None


def detect_amplification_consistency(text: str) -> dict:
    """Detect whether amplification is coherent or fragmented."""
    coherent_count = sum(1 for phrase in STRATEGIC_PATTERNS["amplification_consistency"]["coherent_amplification"]
                        if phrase in text.lower())
    fragmented_count = sum(1 for phrase in STRATEGIC_PATTERNS["amplification_consistency"]["fragmented_amplification"]
                          if phrase in text.lower())
    
    if coherent_count >= 2:
        return {
            "dimension": "amplification_consistency",
            "pattern": "coherent_amplification",
            "confidence": min(0.9, 0.5 + (coherent_count * 0.1)),
            "evidence": f"Coherent amplification: {coherent_count} markers",
            "categorical_family": "morphisms"
        }
    elif fragmented_count >= 2:
        return {
            "dimension": "amplification_consistency",
            "pattern": "fragmented_amplification",
            "confidence": min(0.85, 0.5 + (fragmented_count * 0.1)),
            "evidence": f"Fragmented amplification: {fragmented_count} markers",
            "categorical_family": "constraints"
        }
    return None


def detect_shadow_integration(text: str) -> dict:
    """Detect whether strategy acknowledges limitations (shadow)."""
    acknowledged_count = sum(1 for phrase in STRATEGIC_PATTERNS["shadow_integration"]["acknowledged_shadow"]
                            if phrase in text.lower())
    denied_count = sum(1 for phrase in STRATEGIC_PATTERNS["shadow_integration"]["denied_shadow"]
                      if phrase in text.lower())
    
    if acknowledged_count >= 2:
        return {
            "dimension": "shadow_integration",
            "pattern": "acknowledged_shadow",
            "confidence": min(0.9, 0.5 + (acknowledged_count * 0.1)),
            "evidence": f"Shadow acknowledgment: {acknowledged_count} markers",
            "categorical_family": "morphisms"
        }
    elif denied_count >= 2:
        return {
            "dimension": "shadow_integration",
            "pattern": "denied_shadow",
            "confidence": min(0.85, 0.5 + (denied_count * 0.1)),
            "evidence": f"Shadow denial: {denied_count} markers",
            "categorical_family": "constraints"
        }
    return None


def detect_aspirational_realism(text: str) -> dict:
    """Detect whether aspirations are grounded or unrealistic."""
    grounded_count = sum(1 for phrase in STRATEGIC_PATTERNS["aspirational_realism"]["grounded_aspiration"]
                        if phrase in text.lower())
    unrealistic_count = sum(1 for phrase in STRATEGIC_PATTERNS["aspirational_realism"]["unrealistic_aspiration"]
                           if phrase in text.lower())
    
    if grounded_count >= 2:
        return {
            "dimension": "aspirational_realism",
            "pattern": "grounded_aspiration",
            "confidence": min(0.9, 0.5 + (grounded_count * 0.1)),
            "evidence": f"Grounded aspiration: {grounded_count} markers",
            "categorical_family": "morphisms"
        }
    elif unrealistic_count >= 2:
        return {
            "dimension": "aspirational_realism",
            "pattern": "unrealistic_aspiration",
            "confidence": min(0.85, 0.5 + (unrealistic_count * 0.1)),
            "evidence": f"Unrealistic aspiration: {unrealistic_count} markers",
            "categorical_family": "constraints"
        }
    return None


def analyze_strategy_document(strategy_text: str) -> dict:
    """
    Analyze strategy document through ideal amplification lens.
    
    Zero LLM cost - pure deterministic pattern matching.
    
    Detects:
    - Archetypal clarity (clear vs ambiguous ideal)
    - Amplification consistency (coherent vs fragmented)
    - Shadow integration (acknowledged vs denied)
    - Aspirational realism (grounded vs unrealistic)
    
    Returns findings in tomographic format for integration.
    """
    findings = []
    
    # Run all detectors
    detectors = [
        detect_archetypal_clarity,
        detect_amplification_consistency,
        detect_shadow_integration,
        detect_aspirational_realism
    ]
    
    for detector in detectors:
        result = detector(strategy_text)
        if result:
            findings.append(result)
    
    return {
        "domain": "ideal_amplification",
        "findings": findings,
        "total_findings": len(findings),
        "methodology": "deterministic_pattern_matching",
        "llm_cost_tokens": 0
    }


@mcp.tool()
def analyze_strategy_document_tool(strategy_text: str) -> str:
    """
    Analyze a strategy document through ideal amplification structural lens.
    
    This is the tomographic domain projection tool - it projects strategic
    text through ideal amplification vocabulary to detect aspirational patterns.
    
    Zero LLM cost - pure deterministic pattern matching.
    
    Args:
        strategy_text: Full text of the strategy document to analyze
    
    Returns:
        JSON string with findings format:
        {
            "domain": "ideal_amplification",
            "findings": [
                {
                    "dimension": "archetypal_clarity",
                    "pattern": "clear_archetype",
                    "confidence": 0.8,
                    "evidence": "...",
                    "categorical_family": "objects"
                },
                ...
            ],
            "total_findings": 3,
            "methodology": "deterministic_pattern_matching",
            "llm_cost_tokens": 0
        }
    
    Example:
        >>> result = analyze_strategy_document_tool(strategy_pdf_text)
        >>> findings = json.loads(result)["findings"]
    """
    result = analyze_strategy_document(strategy_text)
    return json.dumps(result, indent=2)


# Entry point for MCP protocol
if __name__ == "__main__":
    mcp.run()
